from Arithmatic import ArithmaticCoding
import os
import pickle
import argparse
import time 
import collections
TERMINATOR = "$"

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

def probability_table(data):

    length_input = len(data)
    low_prob = 0
    freq = collections.Counter(data)
    table = dict()

    for key, value in freq.items():
        _range = value / length_input
        table[key] = (low_prob, low_prob + _range)
        low_prob = low_prob + _range

    return table

def compression_ratio(binary, output_file):
    num = len(binary)
    compressed_size = os.stat(output_file).st_size
    compressed_size = num + compressed_size
    return compressed_size

def main():
    args = option()
    if args["type"] == "encode":

        start_time = time.time()

        with open(args["input"], 'r') as f:
            string = f.read().rstrip("\n")
            # Add the terminator at the end of string
            string += TERMINATOR

        # Create probability table 
        table = probability_table(string)

        # Encode information source 
        ArthCode = ArithmaticCoding(table, "$")
        (value, binary) = ArthCode.Compress(string)

        print("[INFO] The value encoded: {}".format(value))
        print("[INFO] The binary representation: {}".format(binary))

        end_time = time.time()
        print('[INFO] Total run-time: {} ms'.format((end_time - start_time) * 1000))

        with open(args["store"], 'wb') as f:
            pickle.dump(table, f)
    
        with open(args["output"], 'wb') as f:
            pickle.dump((binary, table), f)

        # Number of bits before compressing 
        uncompressed_size = os.stat(args["input"]).st_size
        print('[INFO] Uncompressed size: {} bytes'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = compression_ratio(binary, args["store"])
        print('[INFO] Compressed size: {} bytes'.format(compressed_size))

        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
    
    elif args["type"] == "decode":
        start_time = time.time()

        with open(args["input"], 'rb') as f:
            (code, table) = pickle.load(f)

        print("[INFO] The encoded binary: {}".format(code))

        # Decode Arithmatic string 
        ArthCode = ArithmaticCoding(table, "$")
        result = ArthCode.Decompress(code)
        print("[INFO] Result decode: {}".format(result))

        end_time = time.time()
        print('[INFO] Total run-time: {} ms'.format((end_time - start_time) * 1000))

        # write result file 
        with open(args["output"], 'w+') as f:
            f.write(result)
    else:
        print("Error!!!")

if __name__ == '__main__':
    main()