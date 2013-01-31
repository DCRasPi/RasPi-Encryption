#This file contains all the various KEY decode functions

#We have to find the correct key order


def KeyValue(KeyList, component):

    x = int(KeyList[component], 16)

    return x


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


def OrderKey(keyDict, orderedKeyLis):


        OrderedKeyHash = {}
        numbers = range(0, 4)

        for x in numbers:
                OrderedKeyHash[x] = 0


        i = 0

        while not i == 4:
                n = 0
                while not n == 4:
                        if orderedKeyLis[i] == keyDict[n]:
                                OrderedKeyHash[i] = n
                        n = n + 1
                i = i + 1

        return OrderedKeyHash


def FlipDictionary(Dict):

    iList = range(0, 4)
    FlippedDict = {}

    i = 0

    while not i > 3:
        for value in iList:
            if Dict[value] == i:
                FlippedDict[i] = value

        i = i + 1

    return FlippedDict
        

        


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
    


    
