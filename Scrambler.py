def flip(x):
    if x == 0:
        return 1
    if x == 1:
        return 0

def Scramble(binary):
    msgBinary = binary
    key = "e81e38192bfd4B7e"

    msgBinaryList = list(msgBinary)
    keyList = list(key)
    numRange = range(0,16)


    #Get the numeric values of the key 
    for x in numRange:
        keyList[x] = int(keyList[x],16)




    
    for x in keyList:
        #Find the bit that corresponds to the key.  
        a = msgBinaryList[x]
        b = flip(int(a))
        msgBinaryList[x] = b

    return msgBinaryList
