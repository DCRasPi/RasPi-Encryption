def flip(x):
    if x == 0:
        return 1
    if x == 1:
        return 0

def Scramble(binary,key):
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
        msgBinaryList[int(x)] = b

    return msgBinaryList
