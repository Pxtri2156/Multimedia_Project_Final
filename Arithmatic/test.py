from Arithmatic import ArithmaticCoding
import pickle

def bin_float(string: str):
    whole, dec = string.split(".")
    res = 0
    k = -1
    for digit in dec:
        res += int(digit) * 2**k
        k -= 1
    return res

with open("output.txt", 'rb') as f:
    (code, table) = pickle.load(f)
    print("The encoded binary string: {}".format(code))
    #res = bin_float(code)
    #print("Value: {}".format(res))
    for key in table:
        print(r"""|{:<10}|{:<30}|""".format(str(key), "[{}, {})".format(round(table[key][0], 10), round(table[key][1], 10))))
    ArthCode = ArithmaticCoding(table, "$")
    result = ArthCode.Decompress(code)
    print("Hi: {}".format(result))
    #decoded_string = arithmetic_Decompression(code=code, table=probability_table)
    #print("[INFO] The decoded string: {}".format(decoded_string))