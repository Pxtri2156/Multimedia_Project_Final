
import tkinter as tk
from tkinter import filedialog 
import collections
import ast
import random
from Huffman import Huffman
import os
import pickle
import math

LARGE_FONT= ("Verdana bold", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, bg= "#210F0B" )

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.app_data = {"name":    tk.StringVar(),
                         "address": tk.StringVar()
                        }
        self.frames = {}
        self.value = ""
        for F in (MODE, 
                  COMPRESSION, 
                  DECOMPRESSION, 
                  Arithmetic_encode,
                  Arithmetic_decode, 
                  LZW_encode, 
                  LZW_decode, 
                  Huffman_encode, 
                  Huffman_decode,
                  RLC_encode,
                  RLC_decode,
                  Shanon_Fano_encode,
                  Shanon_Fano_decode):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MODE)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class MODE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg= "#34495E")

        label = tk.Label(self, text="MODE", height =2, width = 20, font=("bold", 20 ), bg = "#F7DC6F")
        

        button = tk.Button(self, text="COMPRESSION", font = "bold",  width = 20,
                            command=lambda: controller.show_frame(COMPRESSION))

        button2 = tk.Button(self, text="DECOMPRESSION", font = "bold",  width = 20,
                            command=lambda: controller.show_frame(DECOMPRESSION))

        listbox = tk.Listbox(self, width = 40, height = 11, font="Helvetica 12 bold", bg= "#5D6D7E",  foreground="white")

        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "          SUBJECT:           MULTIMEDIA      ")
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "          CLASS:                CS232.K21.KHTN")
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "          MEMBERS OF GROUP:       ")
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "             THINH NGUYEN VUONG   -  18520367")
        listbox.insert(tk.END, "             NHAT PHAM LE QUANG    -  18520120       ")
        listbox.insert(tk.END, "             TRI XUAN PHAM                  -  18521530       ")
        listbox.insert(tk.END, "")
        
        label.grid(row = 4, column = 0, columnspan = 2, pady = 50)
        button.grid(row = 5, column = 0, padx = 150 )
        button2.grid(row = 5, column = 1, padx = 150)
        listbox.grid(row = 6, column = 0, columnspan = 2, pady = 70)

class COMPRESSION(tk.Frame):

    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")

        label = tk.Label(self, text="COMPRESSION", width = 25, height = 2, font = ("bold", 20),  bg="#EC7063", foreground= "white")
 
        button1 = tk.Button(self, text="LZW",width = 30, height = 2, font = "bold",
                            command= lambda: controller.show_frame(LZW_encode))


        button2 = tk.Button(self, text="ARITHMETIC",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(Arithmetic_encode))


        button3 = tk.Button(self, text="HUFFMAN",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(Huffman_encode))
      

        button4 = tk.Button(self, text="RLC",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(RLC_encode))
        

        button5 = tk.Button(self, text="SHANON FANO",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(Shanon_Fano_encode))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK", font = "bold",
                         command = lambda:  controller.show_frame(MODE))

        label.grid(row = 0, column = 0, columnspan =2, padx = 100, pady = 50)
        button4.grid(row = 1, column = 0, padx =100, pady = 4)
        button1.grid(row = 1, column = 1, padx =100, pady = 4)
        button3.grid(row = 2, column = 0, padx =100, pady = 4)
        button2.grid(row = 2, column = 1, padx =100, pady = 4)
        button5.grid(row = 3, column = 0, padx =100, pady = 4)
        Back.grid(row = 5, column = 1, pady =30)

class DECOMPRESSION(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#34495E")

        label = tk.Label(self, text="DECOMPRESSION", width = 25, height = 2, font = ("bold", 20),  bg="#EC7063", foreground= "white")
 
        button1 = tk.Button(self, text="LZW",width = 30, height = 2, font = "bold",
                            command= lambda: controller.show_frame(LZW_decode))


        button2 = tk.Button(self, text="ARITHMETIC",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(Arithmetic_decode))


        button3 = tk.Button(self, text="HUFFMAN",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(Huffman_decode))
      

        button4 = tk.Button(self, text="RLC",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(RLC_decode))
        

        button5 = tk.Button(self, text="SHANON FANO",width = 30, height = 2, font = "bold",
                            command=lambda: controller.show_frame(Shanon_Fano_decode))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK", font = "bold",
                         command = lambda:  controller.show_frame(MODE))

        label.grid(row = 0, column = 0, columnspan =2, padx = 100, pady = 50)
        button4.grid(row = 1, column = 0, padx =100, pady = 4)
        button1.grid(row = 1, column = 1, padx =100, pady = 4)
        button3.grid(row = 2, column = 0, padx =100, pady = 4)
        button2.grid(row = 2, column = 1, padx =100, pady = 4)
        button5.grid(row = 3, column = 0, padx =100, pady = 4)
        Back.grid(row = 5, column = 1, pady =30)

###### lzw ######
class LZW_encode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")

        label = tk.Label(self, text="LZW", font=("bold", 20), width=15, bg="#F8C471")
        
        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                  title = "Select a File", 
                                                  filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                               ("all files", 
                                                                "*.*")))
            
            # Change label contents 
            label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
            global link
            link = filename
            #print(link)

        def get_string(link):
            f = open(link, "r")
            return f.read()

        def Take_input(st): 
            
            #print(Compress(INPUT))
            Output.delete('1.0', tk.END)
            Output1.delete('1.0', tk.END)

            input_file = st
            output_file = Compress(st)

            Output.insert(tk.END, output_file)
            
            ###save file ###
            with open('input_file.pickle', 'wb') as f:
                 pickle.dump(input_file, f)

            with open('output_file.pickle', 'wb') as f:
                 pickle.dump(output_file, f)

            input_size = os.stat('input_file.pickle').st_size
            output_size = os.stat('output_file.pickle').st_size
            compress_ratio = input_size/output_size

            Output1.insert(tk.END, "input size: "+ str(input_size) + " bytes")
            Output1.insert(tk.END, "\noutput size: "+ str(output_size) + " bytes")
            Output1.insert(tk.END, "\nratio compresstion: "+ str(round(compress_ratio,2)))
            ###delete file ###
            os.remove("input_file.pickle")
            os.remove("output_file.pickle")

        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 

        inputtxt = tk.Text(self, height = 10, 
                width = 40, 
                bg = "light yellow") 
  
        Output = tk.Text(self, height = 10,  
              width = 40,  
              bg = "light cyan") 

        Output1 = tk.Text(self, height = 3,  
              width = 40,  
              bg = "light cyan")

        Display = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

        Display1 = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda: Take_input(get_string(link)))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda:  controller.show_frame(COMPRESSION))

        label.grid(column = 0, row = 0, columnspan =2, pady =20, padx = 400)
        inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
        label_file_explorer.grid(row = 1, column = 1)
        button_explore.grid(row = 2, column = 1)
        Display.grid(row = 3, column = 0)
        Display1.grid(row = 3, column = 1, padx = 5)
        Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
        Output1.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        Back.grid(row = 6, column = 1, pady = 10)


        def Compress(words):
    
            dictionary_table = { chr(c):c for c in range(0,256) }
            key_list = dictionary_table.keys()
        
            code = 255
            code_list = []
            len_string = len(words)
            index = 0
        
            c = words[index]
        
            while(index < len_string - 1):
            
                s = words[index + 1]
                if c + s not in key_list:
                
                    code += 1
                    dictionary_table[c + s] = code
                    code_list.append(dictionary_table[c])
                    index += 1
                    c = s
            
                else:
                
                    c = c + s
                    index += 1
                
            code_list.append(dictionary_table[c])   
        
            return code_list

class LZW_decode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="LZW", font=("bold", 20), width=15, bg="#F8C471")
        
        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                  title = "Select a File", 
                                                  filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                               ("all files", 
                                                                "*.*")))
            
            # Change label contents 
            label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")
           
            global link
            link = filename
            #print(link)

        def get_string(link):
            f = open(link, "r")
            return f.read()

        def Take_input(st): 
            
            #print(Compress(INPUT))
            Output.delete('1.0', tk.END)

            input_file = st
            output_file = Decompress(st)

            Output.insert(tk.END, output_file)
            
          
        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 

        inputtxt = tk.Text(self, height = 10, 
                width = 40, 
                bg = "light yellow") 
  
        Output = tk.Text(self, height = 10,  
              width = 40,  
              bg = "light cyan") 

        Display = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="DECODE", 
                 command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

        Display1 = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="DECODE", 
                 command = lambda: Take_input(get_string(link)))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda: controller.show_frame(DECOMPRESSION))

        label.grid(column = 0, row = 0, padx = 400, pady =20, columnspan =2)
        inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
        label_file_explorer.grid(row = 1, column = 1)
        button_explore.grid(row = 2, column = 1)
        Display.grid(row = 3, column = 0)
        Display1.grid(row = 3, column = 1, padx = 5)
        Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
        Back.grid(row = 5, column = 1, pady = 10)

        def Decompress(words):
            
            codes  = [int(s) for s in str.split(words) if s.isdigit()] 

            dictionary_table = {c: chr(c) for c in range(0, 256)}
            code = 255
        
            s = ""
            entries = []
            Str = ""
        
            for k in codes:
            
                entry = dictionary_table.get(k, "")
            
                if entry is "":
                    entry = s + s[0]
                Str += entry
            
                if s is not "":
                    code += 1
                    dictionary_table[code] = s + entry[0]
                s = entry
            
            return Str

####### Arithmetic ########
class Arithmetic_encode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="ARITHMETIC", font=("bold", 20), width=15, bg="#F8C471")
        
        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                  title = "Select a File", 
                                                  filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                               ("all files", 
                                                                "*.*")))
            
       
            # Change label contents 
            label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
            global link
            link = filename
            #print(link)

        def get_string(link):
            f = open(link, "r")
            return f.read()

        def Take_input(st): 
            
            #print(Compress(INPUT))
            Output.delete('1.0', tk.END)
            Output1.delete('1.0', tk.END)

            input_file = st
            len_input_file = st
            table_file = probability_table(st)
            output_file = Compress(st,table_file)

            Output.insert(tk.END, output_file)
            
            ###save file ###
            with open('input_file.pickle', 'wb') as f:
                 pickle.dump(input_file, f)

            with open('len_input_file.pickle', 'wb') as f:
                 pickle.dump(output_file, f)

            with open('table_file.pickle', 'wb') as f:
                 pickle.dump(output_file, f)

            with open('output_file.pickle', 'wb') as f:
                 pickle.dump(output_file, f)

            input_size = os.stat('input_file.pickle').st_size
            len_input_size = os.stat('len_input_file.pickle').st_size
            table_size = os.stat('table_file.pickle').st_size
            output_size = os.stat('output_file.pickle').st_size

            compress_ratio = input_size/(output_size + len_input_size + table_size)

            Output1.insert(tk.END, "input size: "+ str(input_size) + " bytes")
            Output1.insert(tk.END, "\noutput size: "+ str(output_size + len_input_size + table_size) + " bytes")
            Output1.insert(tk.END, "\nratio compresstion: "+ str(round(compress_ratio,2)))
            ###delete file ###
            os.remove("input_file.pickle")
            os.remove("len_input_file.pickle")
            os.remove("table_file.pickle")
            os.remove("output_file.pickle")

        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 

        inputtxt = tk.Text(self, height = 10, 
                width = 40, 
                bg = "light yellow") 
  
        Output = tk.Text(self, height = 10,  
              width = 40,  
              bg = "light cyan") 

        Output1 = tk.Text(self, height = 3,  
              width = 40,  
              bg = "light cyan")

        Display = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

        Display1 = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda: Take_input(get_string(link)))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda:  controller.show_frame(COMPRESSION))

        label.grid(column = 0, row = 0, columnspan =2, padx = 400, pady = 20)
        inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
        label_file_explorer.grid(row = 1, column = 1)
        button_explore.grid(row = 2, column = 1)
        Display.grid(row = 3, column = 0)
        Display1.grid(row = 3, column = 1, padx = 5)
        Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
        Output1.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        Back.grid(row = 6, column = 1, pady = 10)
        

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
        #######
        def Compress(word,table):
    
            lowOld = 0.0
            highOld = 1.0
            _range = 1.0
        
        # Iterate through the word to find the final range.
            for c in word:
                low  = lowOld + _range * table[c][0]
                high = lowOld + _range * table[c][1]
                _range = high - low

                # Updete old low & hihh
                lowOld = round(low,10000000000)
                highOld = round(high,10000000000) 
            return round(random.uniform(lowOld, highOld), 10000000000)

class Arithmetic_decode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="ARITHMETIC", font=("bold", 20), width=15, bg="#F8C471")
        label.pack(pady=10,padx=10)
        
        def Take_input(link):
            with open(link, 'rb') as f:
                (number, len_string, table) = pickle.load(f)

            Output.insert(tk.END, Decompress(number, len_string, table)) 
            
        def browseFiles(): 
                filename = filedialog.askopenfilename(initialdir = "/", 
                                                      title = "Select a File", 
                                                      filetypes = (("Text files", 
                                                                    "*.txt*"), 
                                                                   ("all files", 
                                                                    "*.*")))
            
       
                # Change label contents 
                label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

                global link
                link = filename
         
        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 
        Output = tk.Text(self, height = 17,  
              width = 40,  
              bg = "light cyan") 
  
        Display = tk.Button(self,
                 width = 20,  height = 2,
                 text ="DECODE", 
                 command = lambda:Take_input(link)) 

        Back = tk.Button(self, height = 2, width = 10,
                         text = "BACK",
                         command = lambda:  controller.show_frame(DECOMPRESSION))

        label_file_explorer.pack(pady = 40)
        button_explore.pack(pady = 10)
        Display.pack(pady = 10) 
        Output.pack()
        Back.pack(side = tk.RIGHT,pady = 5, padx =380)
        
        
        def Decompress(value, len_string, table):
   
            s = "" # flag to stop the while loop
            result = ""
            for i in range(len_string):
                # find the key which has low <= code and high > code
                for key, t in table.items():
                    if (value >= table[key][0] and value < table[key][1]):
                        result += key 
                        # update low, high, code
                        low = table[key][0]
                        high = table[key][1]
                        _range = high - low
                        value = (value - low)/_range
                        
            return result[0:len_string]

### Huffman ###
class Huffman_encode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="HUFFMAN", font=("bold", 20), width=15, bg="#F8C471")
        
        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                  title = "Select a File", 
                                                  filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                               ("all files", 
                                                                "*.*")))
            
       
            # Change label contents 
            label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
            global link
            link = filename
            #print(link)

        def get_string(link):
            f = open(link, "r")
            return f.read()

        def Take_input(st): 
            
            Output.delete('1.0', tk.END)
            Output1.delete('1.0', tk.END)

            input_file = st
            output_file = Compression(st)
            table_file = collections.Counter(st)

            Output.insert(tk.END, output_file)
            
            ###save file ###
            with open('input_file.pickle', 'wb') as f:
                 pickle.dump(input_file, f)

            with open('output_file.pickle', 'wb') as f:
                 pickle.dump(output_file, f)

            with open('table_file.pickle', 'wb') as f:
                 pickle.dump(table_file, f)

            input_size = os.stat('input_file.pickle').st_size
            output_size = os.stat('output_file.pickle').st_size
            table_size = os.stat('table_file.pickle').st_size
            compress_ratio = input_size/compression_size(output_size,'table_file.pickle')

            Output1.insert(tk.END, "input size: "+ str(input_size) + " bytes")
            Output1.insert(tk.END, "\noutput size: "+ str(compression_size(output_size,'table_file.pickle')) + " bytes")
            Output1.insert(tk.END, "\nratio compresstion: "+ str(round(compress_ratio,2)))
            ###delete file ###
            os.remove("input_file.pickle")
            os.remove("output_file.pickle")


        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        #label_file_explorer.grid(row = 1, column =0) 
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 

        inputtxt = tk.Text(self, height = 10, 
                width = 40, 
                bg = "light yellow") 
  
        Output = tk.Text(self, height = 10,  
              width = 40,  
              bg = "light cyan") 

        Output1 = tk.Text(self, height = 3,  
              width = 40,  
              bg = "light cyan")

        Display = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

        Display1 = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda: Take_input(get_string(link)))#Take_input(browseFiles(get_string)))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda:  controller.show_frame(COMPRESSION))

        label.grid(column = 0, row = 0, pady = 20, padx=400, columnspan =2)
        inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
        label_file_explorer.grid(row = 1, column = 1)
        button_explore.grid(row = 2, column = 1)
        Display.grid(row = 3, column = 0)
        Display1.grid(row = 3, column = 1, padx = 5)
        Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
        Output1.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        Back.grid(row = 6, column = 1, pady = 10)
        #button1 = tk.Button(self, text="BACK TO MODE",
         #                   command= asc)#lambda: controller.show_frame(MODE))
        #button1.pack()
        def compression_size(binary, output_file):
            num = binary
            compressed_size = os.stat(output_file).st_size
            compressed_size = math.ceil(num/8) + compressed_size
            return compressed_size

        def Compression(string):
            freq = collections.Counter(string)
            huff = Huffman(freq)
            binary = huff.Compress(string)
            return binary

class Huffman_decode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="HUFFMAN", font=("bold", 20), width=15, bg="#F8C471")
        label.pack(pady=10,padx=10)
        
        def Take_input(link):
            with open(link, 'rb') as f:
                (code, freq) = pickle.load(f)

            Output.insert(tk.END, Decompression(code,freq)) 
            
        def browseFiles(): 
                filename = filedialog.askopenfilename(initialdir = "/", 
                                                      title = "Select a File", 
                                                      filetypes = (("Text files", 
                                                                    "*.txt*"), 
                                                                   ("all files", 
                                                                    "*.*")))
            
       
                # Change label contents 
                label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
                global link
                link = filename
           
        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 
        Output = tk.Text(self, height = 17,  
              width = 40,  
              bg = "light cyan") 
  
        Display = tk.Button(self,height = 2,
                 width = 20,  
                 text ="DECODE", 
                 command = lambda:Take_input(link)) 

        Back = tk.Button(self, height = 2, width = 10,
                         text = "BACK",
                         command = lambda:  controller.show_frame(DECOMPRESSION))

        label_file_explorer.pack(pady = 40)
        button_explore.pack(pady = 10)
        Display.pack(pady = 10) 
        Output.pack()
        Back.pack(side = tk.RIGHT,pady = 5, padx =380)
        

        def Decompression(code,freq):
   
             huff = Huffman(freq)
             result = huff.Decompress(code)
             return result

###### rlc #####
class RLC_encode(tk.Frame):
        def __init__(self, parent, controller):
            self.controller=controller
            tk.Frame.__init__(self, parent, bg= "#34495E")
            label = tk.Label(self, text="RLC", font=("bold", 20), width=15, bg="#F8C471")
            
            def browseFiles(): 
                filename = filedialog.askopenfilename(initialdir = "/", 
                                                      title = "Select a File", 
                                                      filetypes = (("Text files", 
                                                                    "*.txt*"), 
                                                                   ("all files", 
                                                                    "*.*")))
            
       
                # Change label contents 
                label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
                global link
                link = filename
                #print(link)

            def get_string(link):
                f = open(link, "r")
                return f.read()

            def Take_input(st): 
                Output.delete('1.0', tk.END)
                Output1.delete('1.0', tk.END)

                input_file = st
                output_file, display = Compress(st) 
                Output.insert(tk.END, display)
            
                ###save file ###
                with open('input_file.pickle', 'wb') as f:
                     pickle.dump(input_file, f)

                with open('output_file.pickle', 'wb') as f:
                     pickle.dump(output_file, f)

                input_size = os.stat('input_file.pickle').st_size
                output_size = os.stat('output_file.pickle').st_size
                compress_ratio = input_size/output_size

                Output1.insert(tk.END, "input size: "+ str(input_size) + " bytes")
                Output1.insert(tk.END, "\noutput size: "+ str(output_size) + " bytes")
                Output1.insert(tk.END, "\nratio compresstion: "+ str(round(compress_ratio,2)))
                ###delete file ###
                os.remove("input_file.pickle")
                os.remove("output_file.pickle")


            label_file_explorer = tk.Label(self,  
                                text = "UPLOAD THE FILE", 
                                width = 35, height = 2,  
                                fg = "blue")
            
            button_explore = tk.Button(self,  
                            text = "BROWSE FILES", 
                            command =lambda : browseFiles()) 

            inputtxt = tk.Text(self, height = 10, 
                    width = 40, 
                    bg = "light yellow") 
  
            Output = tk.Text(self, height = 10,  
                  width = 40,  
                  bg = "light cyan") 
  
            Output1 = tk.Text(self, height = 3,  
              width = 40,  
              bg = "light cyan")

            Display = tk.Button(self, height = 2, 
                     width = 20,  
                     text ="ENCODE", 
                     command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

            Display1 = tk.Button(self, height = 2, 
                     width = 20,  
                     text ="ENCODE", 
                     command = lambda: Take_input(get_string(link)))

            Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda:  controller.show_frame(COMPRESSION))

            label.grid(column = 0, row = 0, padx =400, pady =20,columnspan =2)
            inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
            label_file_explorer.grid(row = 1, column = 1)
            button_explore.grid(row = 2, column = 1)
            Display.grid(row = 3, column = 0)
            Display1.grid(row = 3, column = 1, padx = 5)
            Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
            Output1.grid(row = 5, column = 0, columnspan = 2, pady = 10)
            Back.grid(row = 6, column = 1, pady = 10)
           
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
           
            def Compress(string):
                    encode = ""
                    display =""
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
                        encode += string[begin]
                        encode += str(dem)

                        display += string[begin]
                        display +=  "["+str(dem)+"]" 
                    return encode, display

class RLC_decode(tk.Frame):
        def __init__(self, parent, controller):
            self.controller=controller
            tk.Frame.__init__(self, parent, bg= "#34495E")
            label = tk.Label(self, text="RLC", font=("bold", 20), width=15, bg="#F8C471")
            
            def browseFiles(): 
                filename = filedialog.askopenfilename(initialdir = "/", 
                                                      title = "Select a File", 
                                                      filetypes = (("Text files", 
                                                                    "*.txt*"), 
                                                                   ("all files", 
                                                                    "*.*")))
            
       
                # Change label contents 
                label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
                global link
                link = filename
                #print(link)

            def get_string(link):
                f = open(link, "r")
                return f.read()

            def Take_input(st): 
                Output.delete('1.0', tk.END)

                display = Decompress(st)

                Output.insert(tk.END, display)

            label_file_explorer = tk.Label(self,  
                                text = "UPLOAD THE FILE", 
                                width = 35, height = 2,  
                                fg = "blue")
             
            button_explore = tk.Button(self,  
                            text = "BROWSE FILES", 
                            command =lambda : browseFiles()) 

            inputtxt = tk.Text(self, height = 10, 
                    width = 40, 
                    bg = "light yellow") 
  
            Output = tk.Text(self, height = 10,  
                  width = 40,  
                  bg = "light cyan") 
  

            Display = tk.Button(self, height = 2, 
                     width = 20,  
                     text ="DECODE", 
                     command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

            Display1 = tk.Button(self, height = 2, 
                     width = 20,  
                     text ="DECODE", 
                     command = lambda: Take_input(get_string(link)))

            Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda:  controller.show_frame(DECOMPRESSION))

            label.grid(column = 0, row = 0, padx = 400, pady =20, columnspan =2)
            inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
            label_file_explorer.grid(row = 1, column = 1)
            button_explore.grid(row = 2, column = 1)
            Display.grid(row = 3, column = 0)
            Display1.grid(row = 3, column = 1, padx = 5)
            Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
            Back.grid(row = 5, column = 1, pady = 10)
            
            def Decompress(string):
                    
                    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    display =""
                    index = 0
                    char = ""
                    num = ""
                    flag = True
                    len_string = len(string)
                    while index < len_string:
                        if string[index] not in num_list:
                            if flag:
                                char = string[index]
                                flag = False
                            else:
                                len_st = int(num)
                                for i in range(len_st):
                                    display += char
                                char = string[index]
                                num =""
                        else:
                            num += string[index]

                        index += 1

                    len_st = int(num)
                    for i in range(len_st):
                        display += char

                    return display
####### shanon fano ####
class Shanon_Fano_encode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="SHANON FANO", font=("bold", 20), width=15, bg="#F8C471")
       
        
        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                  title = "Select a File", 
                                                  filetypes = (("Text files", 
                                                                "*.txt*"), 
                                                               ("all files", 
                                                                "*.*")))
            
       
            # Change label contents 
            label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
            global link
            link = filename
            #print(link)

        def get_string(link):
            f = open(link, "r")
            return f.read()

        def Take_input(st): 
            
            Output.delete('1.0', tk.END)
            Output1.delete('1.0', tk.END)

            input_file = st
            output_file = Compress(st)
            table_file = collections.Counter(st)

            Output.insert(tk.END, output_file)
            
            ###save file ###
            with open('input_file.pickle', 'wb') as f:
                 pickle.dump(input_file, f)

            with open('output_file.pickle', 'wb') as f:
                 pickle.dump(output_file, f)

            with open('table_file.pickle', 'wb') as f:
                 pickle.dump(table_file, f)

            input_size = os.stat('input_file.pickle').st_size
            output_size = os.stat('output_file.pickle').st_size
            table_size = os.stat('table_file.pickle').st_size
            compress_ratio = input_size/compression_size(output_size,'table_file.pickle')

            Output1.insert(tk.END, "input size: "+ str(input_size) + " bytes")
            Output1.insert(tk.END, "\noutput size: "+ str(compression_size(output_size,'table_file.pickle')) + " bytes")
            Output1.insert(tk.END, "\nratio compresstion: "+ str(round(compress_ratio,2)))
            ###delete file ###
            os.remove("input_file.pickle")
            os.remove("output_file.pickle")


        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
       
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles()) 

        inputtxt = tk.Text(self, height = 10, 
                width = 40, 
                bg = "light yellow") 
  
        Output = tk.Text(self, height = 10,  
              width = 40,  
              bg = "light cyan") 

        Output1 = tk.Text(self, height = 3,  
              width = 40,  
              bg = "light cyan")

        Display = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda:Take_input(inputtxt.get("1.0", "end-1c") )) 

        Display1 = tk.Button(self, height = 2, 
                 width = 20,  
                 text ="ENCODE", 
                 command = lambda: Take_input(get_string(link)))

        Back = tk.Button(self, height = 2,
                         width = 20, 
                         text = "BACK",
                         command = lambda:  controller.show_frame(COMPRESSION))

        label.grid(column = 0, row = 0, columnspan =2, pady = 20, padx =400)
        inputtxt.grid(row = 1, column = 0, rowspan = 2, padx= 10, pady =10)
        label_file_explorer.grid(row = 1, column = 1)
        button_explore.grid(row = 2, column = 1)
        Display.grid(row = 3, column = 0)
        Display1.grid(row = 3, column = 1, padx = 5)
        Output.grid(row = 4, column = 0, columnspan = 2, pady = 10)
        Output1.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        Back.grid(row = 6, column = 1, pady = 10)
        
        def compression_size(binary, output_file):
            num = binary
            compressed_size = os.stat(output_file).st_size
            compressed_size = math.ceil(num/8) + compressed_size
            return compressed_size

        def Build_Tree(list,begin,end):

            ''' 
            This function bulid tree Shannon Fano 
            Actualy tree is list
            '''
            i = begin 
            if begin <  end:
                while Sum_List(list,begin,i) < Sum_List(list,i+1,end):
                    i += 1
        
                # add code 
                for j in range(begin,i+1):
                    list[j].append(0)
                for j in range(i+1,end+1):
                    list[j].append(1)

                # Split list 
                return Build_Tree(list,begin,i), Build_Tree(list,i+1, end)
            else:
                return list

        def Sum_List(list,begin,end):
    
            '''
            This function calculate sum list from begin to end
            '''
            s = list[begin][1]
            for i in range(begin+1,end+1):
                s += list[i][1]
            return s

        def Sum(Tree):
            s = 0 
            for i in Tree:
                s += i[1]
            return s

        def Compress(string):
            encode = ""
            '''
            This function compression
            '''
            #print('Do')
            Tree = []
            l = len(string)
            i = 0
            while Sum(Tree) < l:
                #print('Xuong')
                while string[i] in [row[0] for row in Tree]:
                    i = i+1
                #print('i',i)
                Tree.append([string[i],string.count(string[i])])
                i = i+1
            #print(Tree)

            # Sort
            Tree.sort(key=lambda Tree: Tree[1],reverse=1)

            # Build Tree 
            len_l = len(Tree)
            Build_Tree(Tree,0,len_l-1)

            # Convert list to dictionary
            dict = {}
            for i in range(len_l):
                dict[Tree[i][0]] = Tree[i][1:]
            Tree = dict
            #print('Shannon Fano Tree',self.Tree)

            # Covert code for Shannon Fano
            for i in range(l):
                temp_str = ''
                for char in Tree[string[i]][1:]:
    
                    temp_str = temp_str + str(char)
                encode += temp_str
            #pickle.dump(self.encode,open(path_save_code,'wb'))
            # Create Table Probability
            Table = {}
            for key in Tree.keys():
                Table[key] = Tree[key][0]
            #print('TABLE Probability: ', Table)

            #pickle.dump(self.Tree,open(path_save_tree,'wb'))
            #pickle.dump(Table,open(path_save_tree,'wb'))
            #self.B1 = math.ceil(len(self.encode)/8) + os.stat(path_save_tree).st_size
            return encode

class Shanon_Fano_decode(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent, bg= "#34495E")
        label = tk.Label(self, text="SHANON FANO", font=("bold", 20), width=15, bg="#F8C471")
        label.pack(pady=10,padx=10)
        
        def Take_input():
            
            #with open("Tree(1).txt", 'rb') as f:
                #(freq) = pickle.load(f)

            with open(link, 'rb') as f:
                (code,freq) = pickle.load(f)
                

            Output.insert(tk.END, Decompression(code,freq)) 
            
        def browseFiles(): 
                filename = filedialog.askopenfilename(initialdir = "/", 
                                                      title = "Select a File", 
                                                      filetypes = (("Text files", 
                                                                    "*.txt*"), 
                                                                   ("all files", 
                                                                    "*.*")))
            
       
                # Change label contents 
                label_file_explorer.configure(text="UPLOADED SUCCESSFULLY!")

           
                global link
                link = filename
            #table = ast.literal_eval(INPUT2) 
            
       
        label_file_explorer = tk.Label(self,  
                            text = "UPLOAD THE FILE", 
                            width = 35, height = 2,  
                            fg = "blue")
        #label_file_explorer.grid(row = 1, column =0) 
        button_explore = tk.Button(self,  
                        text = "BROWSE FILES", 
                        command =lambda : browseFiles())
        
        Output = tk.Text(self, height = 17,  
              width = 40,  
              bg = "light cyan") 
  
        Display = tk.Button(self, height = 2,
                 width = 20,  
                 text ="DECODE", 
                 command = lambda:Take_input()) 

        Back = tk.Button(self, height = 2, width = 10,
                         text = "BACK",
                         command = lambda:  controller.show_frame(DECOMPRESSION))

        label_file_explorer.pack(pady = 40)
        button_explore.pack(pady = 10)
        Display.pack(pady = 10) 
        Output.pack()
        Back.pack(side = tk.RIGHT,pady = 5, padx =380)

        def Decompression(encode,Tree):
        
            decode =""
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
                        return decode
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
                        decode = decode + key
                        break
                low = high
                high += 1
            
            return decode   
        
app = SeaofBTCapp()
app.mainloop()