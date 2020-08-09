from Huffman import Huffman
import os
import collections
import pickle
import argparse
import time 
import utility
import math

def option():
    ap = argparse.ArgumentParser(description="The Aritmetic algorithm")
    ap.add_argument("-t", "--type", required=True,
                    choices=['encode', 'decode'],
                    help="Choice Encode or Decode")
    ap.add_argument("-i", "--input", required=True,
                help="path to input of encode/ path to input of decode")
    ap.add_argument("-o", "--output", required=True,
                help="path to output of encode/ path to output of decode")
    ap.add_argument("-s", "--store", default="store.txt",
                help="path to store table of encode")
    args = vars(ap.parse_args())
    return args

def compression_ratio(binary, output_file):
    num = len(binary)
    compressed_size = os.stat(output_file).st_size
    compressed_size = math.ceil(num/8) + compressed_size
    return compressed_size

def main():

    args = option()
    if args["type"] == "encode":
        start_time = time.time()

        with open(args["input"], 'r') as f:
            string = f.read()

        # Get frequency table from data
        freq = collections.Counter(string)
        huff = Huffman(freq)
        binary = huff.Compress(string)
        end_time = time.time()

        print("[INFO] The binary representation: {}".format(binary))
        print('[INFO] Total run-time: {} ms'.format((end_time - start_time) * 1000))

        with open(args["store"], 'wb') as f:
            pickle.dump(freq, f)

        with open(args["output"], 'wb') as f:
            pickle.dump((binary, freq), f)
                
        # Number of bits before compressing 
        uncompressed_size = os.stat(args["input"]).st_size
        print('[INFO] Uncompressed size: {} bytes'.format(uncompressed_size))
        
        compressed_size = compression_ratio(binary, args["store"])
        print('[INFO] Compressed size: {} bytes'.format(compressed_size))
        
        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
    
    elif args["type"] == "decode":
        start_time = time.time()

        with open(args["output"], 'rb') as f:
            (code, freq) = pickle.load(f)

        print("[INFO] The encoded binary: {}".format(code))

        huff = Huffman(freq)
        result = huff.Decompress(code)
        end_time = time.time()
        
        print("[INFO] Result decode: {}".format(result))
        print('[INFO] Total run-time: {} ms'.format((end_time - start_time) * 1000))

        # write result file 
        with open(args["output"], 'w+') as f:
            f.write(result)
    else:
        print("Error!!!")

if __name__ == '__main__':
    main()

    
