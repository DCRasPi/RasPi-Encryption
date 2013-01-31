import BinaryDecode
import KeyDecode
import KeyGenerator



def ReArrangeBit(BinaryKeyTable, OrderedKeyHash):
    BinaryString = ['0', '0', '0', '0']
    i = 0
    n = 0
    
    


    while not n > 3:
        i = 0
        while not i > 3:
            if OrderedKeyHash[i] == n:
                BinaryString[n] = BinaryKeyTable[i]
            i = i + 1
        n = n + 1
        

    return BinaryString


def RetrieveBinaryTable(NumberList, Key):
    UBinTable = BinaryDecode.BinaryList(NumberList)
    UOrderList = KeyDecode.OrderByKeyList(Key)
    UOrderKey = KeyDecode.OrderKey(Key, UOrderList)
    OrderKey = KeyDecode.FlipDictionary(UOrderKey)
    BinaryStrList = ReArrangeBit(UBinTable, OrderKey)
    BinaryString = StickTogether(BinaryStrList)

    return BinaryString

    

def StickTogether(binarystrlist):
    return "".join(binarystrlist)



def flip(x):
    if x == 0:
        return 1
    if x == 1:
        return 0

def FlipBits(binary,key):
    msgBinary = binary
    BitKey = key
    msgBinaryList = list(msgBinary)
    keyList = list(BitKey)
    numRange = range(0,16)

    for x in numRange:
        keyList[x] = int(keyList[x],16)

    for x in keyList:
        a = msgBinaryList[int(x)]
        b = flip(int(a))
        msgBinaryList[int(x)] = str(b)
    

    
    return msgBinaryList

def Decrypt(NumberList, key):
    BinString = RetrieveBinaryTable(NumberList, key)
    KeyString = "".join(KeyGenerator.ConvertToList(key))

    bitlist = FlipBits(BinString, KeyString)

    string1 = "".join(bitlist[0:8])
    string2 = "".join(bitlist[8:16])

    char1 = chr(int(string1, 2))
    char2 = chr(int(string2, 2))

    charstring = char1 + char2

    return charstring
    

    
