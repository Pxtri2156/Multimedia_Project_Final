from Arithmatic import ArithmaticCoding
import os
import pickle
import argparse
import time 
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
    args = vars(ap.parse_args())
    return args

def probability_table(infomation_source):

    count_frequencies = dict()
    table = dict()

    for value in infomation_source:
        if value in count_frequencies:
            count_frequencies[value] += 1
        else:
            count_frequencies[value] = 1

    count_sum = len(infomation_source)

    low_prob = 0

    for key in count_frequencies:
        range = count_frequencies[key] / count_sum
        table[key] = (low_prob, low_prob + range)
        low_prob = low_prob + range

    return table

def main():
    args = option()
    if args["type"] == "encode":

        start_time = time.time()

        with open("test.txt", 'r') as f:
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

        with open(args["output"], 'wb') as f:
            pickle.dump((binary, table), f)

        # Number of bits before compressing 
        uncompressed_size = os.stat("test.txt").st_size
        print('Uncompressed size: {} bytes'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = os.stat("output.txt").st_size
        print('Compressed size: {} bytes'.format(compressed_size))

        # Calculate compression ratio 
        print('Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
        end_time = time.time()
        print('total run-time: {} ms'.format((end_time - start_time) * 1000))

    elif args["type"] == "decode":
        start_time = time.time()

        with open(args["input"], 'rb') as f:
            (code, table) = pickle.load(f)

        print("The encoded binary: {}".format(code))

        # Decode Arithmatic string 
        ArthCode = ArithmaticCoding(table, "$")
        result = ArthCode.Decompress(code)
        print("Result decode: {}".format(result))

        end_time = time.time()
        print('total run-time: {} ms'.format((end_time - start_time) * 1000))

        # write result file 
        with open(args["output"], 'w+') as f:
            f.write(result)
    else:
        print("Error!!!")

if __name__ == '__main__':
    main()