import os
import  pickle

class Shannon_Fano:
    
    def __init__(self):
        self.Tree = []
        self.encode = []
        self.decode = []
        self.B0 = None
        self.B1 = None

    def Compression(self,str,path_save_code,path_save_tree):
        '''
        This function compression
        '''
        #print('Do')
        Tree = []
        l = len(str)
        i = 0
        while self.Sum(Tree) < l:
            #print('Xuong')
            while str[i] in [row[0] for row in Tree]:
                i = i+1
            #print('i',i)
            Tree.append([str[i],str.count(str[i])])
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
            self.encode = self.encode + (self.Tree[str[i]][1:])
        pickle.dump(encode,open(path_save_code,'wb'))
        prikcle.dump(self.Tree,open(path_save_tree,'wb'))
        self.B0 = 
        return self.encode

    def Decompression(self,code,Tree,path_save_decode):
        result = ''
        low = 0 
        high = 1
        len_code = len(code)
        while low < len_code:
            while code[low:high] not in [Tree[key][1:] for key in Tree.keys() ]:
                #print(code[low:high])
                if high >= len_code:
                    return result
                high += 1
            #print('low {low} high {high}'.format(low = low, high = high))
            for key in Tree.keys():
                if Tree[key][1:] != code[low:high]:
                    continue
                else:
                    #print(key)
                    result = result + key
                    break
            low = high
            high += 1
        pickle.dump(result,open(path_save_decode,'wb'))
        return result
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

    def Compression_Ratio(self,str):
        return self.B0/self.B1

      