from Shannon_Fano import Shannon_Fano
from RunLenghtCoding import RLC

with open('../Huffman/test.txt','r', encoding="utf8") as fb:
    str = fb.read()
    print('input file',str)
R = RLC()
S = Shannon_Fano()
choose = input("Enter choose:s ")
if choose == 'y':
    code = S.Compression(str,'encode.txt','Tree.txt')
    print('Code after compression: ',code)
    decode = S.Decompression(code,S.Tree,'Decode.txt')
    print('String after decompression',decode)
    print('Compression ratio: ',S.Compression_Ratio())
else:
    encode = R.Compression(str,'encode.txt')
    print('Code after compression: ',encode)
    decode = R.Decompression(encode,'Decode.txt')
    print('String after decompression',decode)
    print('Compression ratio: ',R.Compression_Ratio())


