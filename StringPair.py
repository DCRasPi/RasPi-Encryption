import math


  

def KeyPairs(string):
    Char1 = string[0:1]
    Char2 = string[1:]

    


    Bintemp1 = bin(ord(Char1))
    Bintemp2 = bin(ord(Char2))

    Bin1 = (Bintemp1[0:1] + Bintemp1[2:])
    Bin2 = (Bintemp2[0:1] + Bintemp2[2:])

    while len(Bin1) < 8:
        Bin1 = '0' + Bin1

    while len(Bin2) < 8:
        Bin2 = '0' + Bin2

    BinaryString = (Bin1 + Bin2)

    return BinaryString
    
    
    


def ConvertToTable(BinaryString): #Joe says I should make a comment
    #No-one listens to Joe anyway

    KeyBinDict = {}
    i = 0
    a = 0
    while not i == 4:
        TempKeyList = []
        while not a == 4:                    
            TempKeyList.append((BinaryString[a:(a+1)]))
            a = a + 1
            
        KeyBinDict[i] = TempKeyList
        a = 0
        i = i + 1

    return KeyBinDict





