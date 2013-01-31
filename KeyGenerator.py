
import random
import math

def KeyGenerator():
    KeyListDict = {}
    i = 0
    a = 0

    while not i == 4:
        TempKeyList = []
        while not a == 4:

            tempRandom = random.randrange(1, 16)
            keytemp = hex(tempRandom)[2:]
            TempKeyList.append(keytemp)
            a = a + 1
            
        KeyListDict[i] = "".join(TempKeyList)
        a = 0
        i = i + 1

        
          

    return KeyListDict


def KeyValue(KeyList, component):

    x = int(KeyList[component], 16)

    return x




def OrderToKeyLocation(Key):
    n = 0
    while not n == 4:
        for value in Key[n]:
            KeyList.append(value)
        n = n + 1

    return KeyList



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

def ConvertToList(Key):
    Keylist = []
    i = 0
    n = 0
    while not i == 4:
        n = 0
        while not n > 3:
            if n == 3:
                tempstring = Key[i][n:]
            else:
                tempstring = Key[i][n:(n+1)]
            Keylist.append(tempstring)
            n = n + 1
        i = i + 1

    return Keylist
            




    


    
    
    
