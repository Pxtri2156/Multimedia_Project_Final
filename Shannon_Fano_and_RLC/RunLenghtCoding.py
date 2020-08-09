import os
import  pickle

class RLC:

    def __init__(self):
        self.B0 = None
        self.B1 = None
        self.encode = ''
        self.decode = ''
    def Compression(self,string,path_save):
        l = len(string)
        i = 0
        while i < l:
            begin = i
            dem = 0
            if begin < l:
                pass
            else:
                begin = i
            for j in range(begin,l):
                if string[begin] != string[j]:
                    break
                else:
                    dem += 1
                i += 1
            self.encode = self.encode + string[begin]
            self.encode = self.encode + str(dem)            
        with open(path_save,'wb') as fb:
                pickle.dump(self.encode,fb)
        fb.close()
        self.B1 = len(self.encode)
        self.B0 = l 
        return self.encode

    def Decompression(self,file_path_decompressed):
        l = len(self.encode)
        print(self.encode)
        for i in range(0,l,2):
            F = self.encode[i+1]
            F = int(F)
            for j in range(F):
                self.decode = self.decode + self.encode[i]
        pickle.dump(self.decode,open(file_path_decompressed,'wb'))
        print('len kq',len(self.decode))
        print(self.decode)
        return self.decode
    def Compression_Ratio(self):
        return self.B0/self.B1