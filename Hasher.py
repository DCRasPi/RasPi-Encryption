import hashlib

def HashString(cipherstring):
    CipherHash = hashlib.sha224(cipherstring).hexdigest()

    return CipherHash

def GetString(cipherlist):

    cipherstring = ""

    for x in cipherlist:
        cipherstring = cipherstring + str(x)

    return cipherstring
    

