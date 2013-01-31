#This file contains all the functions needed to encrypt a string
#It does not contain key generation functions
#Import this file to use in the main one






def flip(x):
    if x == 0:
        return 1
    if x == 1:
        return 0

def FlipBits(binary,key):
    msgBinary = binary
    BitKey = key
    msgBinaryList = list(msgBinary)
    keyList = list(BitKey) #Get a list of the key
    numRange = range(0,16)
    CipherBlockChain = 0

    for x in numRange:
        keyList[x] = int(keyList[x],16) 

    for x in keyList:
        a = msgBinaryList[int(x)]
        b = flip(int(a))
        msgBinaryList[int(x)] = str(b)
    

    
    return msgBinaryList

def TableBits(binarylist):
    TabledList = ['0', '0', '0', '0']

    TabledList[0] = binarylist[0:4]
    TabledList[1] = binarylist[4:8]
    TabledList[2] = binarylist[8:12]
    TabledList[3] = binarylist[12:16]

    return TabledList





def OrderKey(keyDict, orderedKeyStr):


        OrderedKeyHash = {}
        numbers = range(0, 4)

        for x in numbers:
                OrderedKeyHash[x] = 0


        i = 0

        while not i == 4:
                n = 0
                while not n == 4:
                        if orderedKeyStr[i] == keyDict[n]:
                                OrderedKeyHash[i] = n
                        n = n + 1
                i = i + 1

        return OrderedKeyHash


def OrderByKeyList(Key):
    i = 0
    templist = []
    orderedhexlist = []
    while not i == 4:
        templist.append(KeyValue(Key, i))
        i = i + 1

    templist = sorted(templist, reverse=True)

    for value in templist:
        orderedhexlist.append(hex(value)[2:])

    return orderedhexlist


def KeyValue(KeyList, component):

    x = int(KeyList[component], 16)

    return x





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

def ReturnNumerics(FinalString):

    tempstring = ''
    i = 0
    while not i > 3:
        tempstring = tempstring + ("".join(FinalString[i]))
        i = i + 1

    numberlist = []
    numberlist.append(int(tempstring[0:4], 2))
    numberlist.append(int(tempstring[4:8], 2))
    numberlist.append(int(tempstring[8:12], 2))
    numberlist.append(int(tempstring[12:16], 2))
      
    
    

    return numberlist


    




    
    

