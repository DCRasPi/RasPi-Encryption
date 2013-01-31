

#This module will scramble a string, but the first and last letters will remain
from random import shuffle

def ScrambleString(string):

    if len(string) > 3:
        stringscramble = string[1:-1]
        prependchar = string[0]
        appendchar = string[-1]


        liststring = list(stringscramble)

        shuffle(liststring)

        tempstring = "".join(liststring)

        Finalstring = prependchar + tempstring + appendchar

        return Finalstring

    else:

        return string

    
