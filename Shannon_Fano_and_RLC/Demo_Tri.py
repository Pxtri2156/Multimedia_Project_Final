from Shannon_Fano import Shannon_Fano
from RunLenghtCoding import RLC


R = RLC()
S = Shannon_Fano()
code = S.Compression('AAAdlka;lkjf;lajBBBCBA')
print('Code after compression: ',code)
decode = S.Decompression(code,S.Tree)
print('String after decompression',decode)