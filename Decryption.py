
import DecodeMain


def BinaryString(integer):
    string = bin(integer)[2:]


def GetBitDict(binarystring):


    binarylist = list(binarystring)
    binarydict = {}

    while len(binarylist) < 16:
        binarylist.insert(0, '0')


    binarystring = "".join(binarylist)



    binarydict[0] = binarystring[0:4]
    binarydict[1] = binarystring[4:8]
    binarydict[2] = binarystring[8:12]
    binarydict[3] = binarystring[12:16]

    return binarydict




def PutItBackTogether(unordereddict, KeyOrder):


    binaryreplaced = {}
    binaryreplaced[0] = ''
    binaryreplaced[1] = ''
    binaryreplaced[2] = ''
    binaryreplaced[3] = ''


    i = 0

    while not i > 3:
        if KeyOrder[i] == 0:
            binaryreplaced[0] = unordereddict[i]
            
        if KeyOrder[i] == 1:
            binaryreplaced[1] = unordereddict[i]
            
        if KeyOrder[i] == 2:
            binaryreplaced[2] = unordereddict[i]
            
        if KeyOrder[i] == 3:
            binaryreplaced[3] = unordereddict[i]

        i = i + 1


    return binaryreplaced






def UnChain(cipherlist):

    truecipherlist = []
    IV = 0
    n = 0
    while not n == len(cipherlist):
        if n == 0:
            truecipherlist.append((cipherlist[n] + IV))
        else:
            truecipherlist.append((cipherlist[n] - cipherlist[n-1])%16)
        n = n + 1


    numberlist = []
    i = 0
    while not (i+4) > len(truecipherlist):
        numberlist.append(truecipherlist[i:(i+4)])
        i = i + 4


    return numberlist

def Decipher(cipherlist, Key):

        
    cList = UnChain(cipherlist)
    Plaintext = ""
    for value in cList:
        Plaintext = Plaintext + (DecodeMain.Decrypt(value, Key))
    
          

        
    
    
    

    return Plaintext
                        


    
    


    
    
