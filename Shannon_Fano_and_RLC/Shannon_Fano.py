import os
import  pickle
import math
import string

class Shannon_Fano:
    
    def __init__(self):
        self.Tree = []
        self.encode = ''
        self.decode = ''
        self.B0 = None
        self.B1 = None

    def Compression(self,string,path_save_code,path_save_tree,path_save_output):
        '''
        This function compression
        '''
        #print('Do')
        Tree = []
        l = len(string)
        i = 0
        while self.Sum(Tree) < l:
            #print('Xuong')
            while string[i] in [row[0] for row in Tree]:
                i = i+1
            #print('i',i)
            Tree.append([string[i],string.count(string[i])])
            i = i+1
        print(Tree)

        # Sort
        Tree.sort(key=lambda Tree: Tree[1],reverse=1)

        # Build Tree 
        len_l = len(Tree)
        self.Build_Tree(Tree,0,len_l-1)

        # Convert list to dictionary
        dict = {}
        for i in range(len_l):
            dict[Tree[i][0]] = Tree[i][1:]
        self.Tree = dict
        print('Shannon Fano Tree',self.Tree)

        # Covert code for Shannon Fano
        for i in range(l):
            temp_str = ''
            for char in self.Tree[string[i]][1:]:
    
                temp_str = temp_str + str(char)
            self.encode = self.encode + temp_str
        pickle.dump(self.encode,open(path_save_code,'wb'))
        # Create Table Probability
        Table = {}
        for key in self.Tree.keys():
            Table[key] = self.Tree[key][0]
        print('TABLE Probability: ', Table)

        #pickle.dump(self.Tree,open(path_save_tree,'wb'))
        pickle.dump(Table,open(path_save_tree,'wb'))
        self.B1 = math.ceil(len(self.encode)/8) + os.stat(path_save_tree).st_size
        pickle.dump((self.encode,Table),open(path_save_output,'wb'))
        return self.encode

    def Decompression(self,encode,Tree,path_save_decode):
        
        low = 0 
        high = 1
        len_code = len(encode)
        Region_Find = []
        for key in Tree.keys():
            temp = ''
            for char in Tree[key][1:]:
                temp = temp + str(char)
            Region_Find.append(temp)
        #print('Region_Find',Region_Find)
        while low < len_code:
            while encode[low:high] not in Region_Find :
                #print(code[low:high])
                if high >= len_code:
                    return self.decode
                high += 1
            #print('low {low} high {high}'.format(low = low, high = high))
            for key in Tree.keys():
                temp = ''
                for char in Tree[key][1:]:
                    temp = temp + str(char)
                if temp != encode[low:high]:
                    continue
                else:
                    #print(key)
                    self.decode = self.decode + key
                    break
            low = high
            high += 1
        pickle.dump(self.decode,open(path_save_decode,'wb'))
        self.B0 = os.stat(path_save_decode).st_size
        #print('len result', len(result))
        return self.decode
        # Thông báo lỗi nếu ko giải nén được file
        # Lưu vào file mặc định 

    def Build_Tree(self,list,begin,end):

        ''' 
        This function bulid tree Shannon Fano 
        Actualy tree is list
        '''
        i = begin 
        if begin <  end:
            while self.Sum_List(list,begin,i) < self.Sum_List(list,i+1,end):
                i += 1
        
            # add code 
            for j in range(begin,i+1):
                list[j].append(0)
            for j in range(i+1,end+1):
                list[j].append(1)

            # Split list 
            return self.Build_Tree(list,begin,i), self.Build_Tree(list,i+1, end)
        else:
            return list

    def Sum_List(self,list,begin,end):
    
        '''
        This function calculate sum list from begin to end
        '''
        s = list[begin][1]
        for i in range(begin+1,end+1):
            s += list[i][1]
        return s
    def Sum(self,Tree):
        s = 0 
        for i in Tree:
            s += i[1]
        return s

    def Compression_Ratio(self):
        print('B0 {B0}, B1 {B1}'.format(B0 = self.B0, B1 = self.B1 ))
        return self.B0/self.B1

      