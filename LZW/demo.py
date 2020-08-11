from LZW import LZWCoding
import os
import collections
import pickle
import argparse
import time 
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
    args = vars(ap.parse_args())
    return args

def main():
    args = option()
    if args["type"] == "encode":
        start_time = time.time()
        with open(args["input"], 'r') as f:
            string = f.read()

        lzw = LZWCoding()
        values = lzw.Compress(string)
        end_time = time.time()
        
        print("[INFO] The value encoded: {}".format(values))
        print('[INFO] Total run-time: {} ms'.format((end_time - start_time) * 1000))
        #values = dict(values)
        print(type(values))
        with open(args["output"], 'wb') as f:
            pickle.dump(values, f)

        # Number of bits before compressing 
        uncompressed_size = os.stat(args["input"]).st_size
        print('[INFO] Uncompressed size: {} bytes'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = os.stat(args["output"]).st_size
        print('[INFO] Compressed size: {} bytes'.format(compressed_size))

        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))

    elif args["type"] == "decode":
        start_time = time.time()

        with open(args["input"], 'rb') as f:
            data = pickle.load(f)

        lzw = LZWCoding()

        result = lzw.Decompress(data)
        end_time = time.time()

        print("[INFO] Result decode: {}".format(result))
        print('[INFO] Total run-time: {} ms'.format((end_time - start_time) * 1000))

        # write result file 
        with open(args["output"], 'w+') as f:
            f.write(result)

if __name__ == '__main__':
    main()
        