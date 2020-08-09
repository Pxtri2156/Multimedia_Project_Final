import os
import  pickle

class RLC:

    def __init__(self):
        self.B0 = None
        self.B1 = None
    def Compression(self,str,path_save):

        kq = []
        l = len(str)
        i = 0
        while i < l:
            begin = i
            dem = 0
            if begin < l:
                pass
            else:
                begin = i
            for j in range(begin,l):
                if str[begin] != str[j]:
                    break
                else:
                    dem += 1
                i += 1
            kq.append(str[begin])
            kq.append(dem)
        with open(path_save,'wb') as fb:
                pickle.dump(kq,fb)
        fb.close()
        return kq

    def Decompression(self,str,file_path_decompressed):
        l = len(str)
        print(str)
        kq = ''
        for i in range(0,l,2):
            F = str[i+1]
            for j in range(F):
                kq = kq + str[i]
        pickle.dump(kq,open(file_path_decompressed,'wb'))
        return kq
    def Compression_Ratio(self):
        return self.Bo/self.B1