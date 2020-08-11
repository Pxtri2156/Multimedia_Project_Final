class ArithmaticCoding:
    def __init__(self, table, terminator):
        self.table = table
        self.terminator = terminator 

    def __GetBinaryFractionValue(self, binaryFraction):
        value = 0
        power = 1

        # Git the fraction bits after "."
        fraction = binaryFraction.split('.')[1]
        # Compute the formula value
        for i in fraction:
            value += ((2 ** (-power)) * int(i))
            power += 1
        return (value, fraction)

    def binary_to_float(self, code):
        # Git the fraction bits after "."
        whole, decimal = code.split(".")
        value = 0
        k = -1
        for digit in decimal:
            value += int(digit) * 2**k
            k -= 1
        return value
    
    def Compress(self, word):
        lowOld = 0.0
        highOld = 1.0
        _range = 1.0
        
        # Iterate through the word to find the final range.
        for c in word:
            low  = lowOld + _range * self.table[c][0]
            high = lowOld + _range * self.table[c][1]
            _range = high - low

            # Updete old low & hihh
            lowOld = low
            highOld = high
        # Generating code word for encoder.
        code = ["0", "."] # Binary fractional number
        k = 2             # kth binary fraction bit
        (value, fraction) = self.__GetBinaryFractionValue("".join(code))
        
        while(value < low):
            # Assign 1 to the kth binary fraction bit
            code.append('1')
            (value,fraction) = self.__GetBinaryFractionValue("".join(code))
            if (value >= high):
                # Replace the kth bit by 0
                code[k] = '0'
            (value,fraction) = self.__GetBinaryFractionValue("".join(code))
            k += 1
        string = "0."+fraction
        return (value,string)
    
    def Decompress(self, code):
        value = self.binary_to_float(code)
        s = "" # flag to stop the while loop
        result = ""
        while (s != self.terminator):
            # find the key which has low <= code and high > code
            for key, t in self.table.items():
                if (value >= self.table[key][0] and value < self.table[key][1]):
                    result += key 
                    # update low, high, code
                    low = self.table[key][0]
                    high = self.table[key][1]
                    _range = high - low
                    value = (value - low)/_range
                    # chech for the terminator
                    if (key == self.terminator):
                        s = key
                        break
        return result
         
