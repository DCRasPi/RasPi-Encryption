#This contains all the functions relating to the binary decoding of a file

def splitString(numberString):
    tempString = str(numberString)
    outStringPiv0 = numberString[:4]
    outStringPiv1 = numberString[4:]

    outString0 = outStringPiv0[:2]
    outString1 = outStringPiv0[2:]
    outString2 = outStringPiv1[:2]
    outString3 = outStringPiv1[2:]

    outIntString0 = int(outString0)
    outIntString1 = int(outString1)
    outIntString2 = int(outString2)
    outIntString3 = int(outString3)

    outList = []
    outList.append(outIntString0)
    outList.append(outIntString1)
    outList.append(outIntString2)
    outList.append(outIntString3)

    return outList



def BinaryList(numericlist):
    binarylist = []
    binarylist.append(RetrieveBits(numericlist[0]))
    binarylist.append(RetrieveBits(numericlist[1]))
    binarylist.append(RetrieveBits(numericlist[2]))
    binarylist.append(RetrieveBits(numericlist[3]))
        
        


    return binarylist

def RetrieveBits(integer):
    binarystring = bin(integer)[2:]

    binarylist = list(binarystring)

    while len(binarylist) < 4:
        binarylist.insert(0, '0')

    binarystring = "".join(binarylist)

    return binarystring



def GetBitDict(binary):



    binarystring = "".join(binarylist)



    binarydict[0] = binarystring[0:4]
    binarydict[1] = binarystring[4:8]
    binarydict[2] = binarystring[8:12]
    binarydict[3] = binarystring[12:16]

    return binarydict

def GetBitString(binarylist):
    return "".join(binarylist)
