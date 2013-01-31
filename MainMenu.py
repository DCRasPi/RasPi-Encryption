#This is the menu. Here are the various options
#There are four options on our menu
#1. Encrypt
#2. Decrypt
#3. Marry
import pickle
import Encrypt
import ast
import KeyGenerator
import Decryption
import Hasher

def MainMenu(OptionList):
    x = (len(OptionList))
    i = 0
    while i < x:
        print (str(i + 1) + ").  " + OptionList[i])
        i = i + 1

    choice = raw_input("Choose your option: ")
    truechoice = CheckIfInteger(choice)

    return truechoice

def ConvertKeyToString(KeyDict):

    String = KeyDict[0] + KeyDict[1] + KeyDict[2] + KeyDict[3]
    return String


def ReadThisFile(Filename):


    HashCipherList = []
    HashCipherList.append("")
    HashCipherList.append("")

    Filehandle = open (Filename, 'r')

    tempstring = Filehandle.readline()
    while tempstring != "\n":
        tempstring = tempstring.replace(" ", "")
        tempstring = tempstring[0:10]
        HashCipherList[0] = HashCipherList[0] + tempstring
        tempstring = Filehandle.readline()
    HashCipherList[1] = Filehandle.readline()

    Filehandle.close
    
    return HashCipherList


def CheckIfInteger(choice):

    string = choice
    while True:
        try:
            truechoice = int(string)
            break
        except ValueError:
            string = raw_input("Please enter a number: ")

    return truechoice


def FindKey(Mount):
    Filename = "/media/" + Mount + "/Key/Key.txt"
    Filehandle = open ( Filename, 'r')
    KeyDict = Filehandle.read()
    KeyDict = ast.literal_eval(KeyDict)

    Filehandle.close
   
    return KeyDict
    

    
def NumericCipherList(Cipherstring):
    cipherlist = []
    i = 0

    while not ((i+2) > len(Cipherstring)):
        cipherlist.append(int(Cipherstring[i:(i+2)]))
        i = i + 2
                              
    return cipherlist

def Continue():
    
    print ("Would you like to continue using this program?, 1 for yes, 2 for no.")
    tchoice = CheckIfInteger(raw_input())
    if tchoice == 1:
        loop = 0
    else:
                    
        loop = 1

    return loop
    

def GetKey(Mount):
    print "Would you like to enter a key, or find one from the USB"
    print "1 for enter, 2 for search"
    tchoice = CheckIfInteger(raw_input())
    if tchoice == 1:
        Key = raw_input()
    else:
        Key = FindKey(Mount)

    return Key

def WriteNewKey(Mount, Key):
    Filename = "/media/" + Mount + "/Key/Key.txt"
    Filehandle = open ( Filename, 'w' )
    Filehandle.write("{0: '" + Key[0:4] + "', 1: '" + Key[4:8] + "', 2: '" + Key[8:12] + "', 3: '" + Key[12:16] + "'}")

    Filehandle.close
    return 1
    
def WriteHash(HashW, FileW):

    Filehandle = open (FileW, 'r+')
    Filehandle.seek(0, 2)
    Filehandle.write('\n')
    Filehandle.write(str(HashW))
    Filehandle.close
    return 1
    


def Marry():
    print "Are you Pi 1 or Pi 2 (Pi 1 will generate the key and give it to Pi 2)"
    print "Enter 1 or 2"
    user_input = int(raw_input())

    if user_input == 1:
        NewKey = Encrypt.GenerateKey()
        print "Enter this key into Pi2, word for word"
        print NewKey
    else:
        print "Please enter the key, matching exactly the key that is used"
        NewKey = raw_input()
        NewKey = ast.literal_eval(NewKey)

    return NewKey

def PrintDecryptedText(DecryptedText, filename):
    i = 0
    Filehandle = open (filename, 'w')

    uBound = len(DecryptedText)

    while not (i + 10) > uBound:
        if (i+20) > uBound:
            tempstring = DecryptedText[i:(i+10)] + '\n'
            Filehandle.write(tempstring)
            x = uBound
            tempstring = DecryptedText[(i+10):x]
            Filehandle.write(tempstring)
            i = i + 20
        else:
            tempstring = DecryptedText[i:(i+10)] + '\n'
            Filehandle.write(tempstring)
            i = i + 10

    Filehandle.close
            
    return 1
    
def ConvertToDictionary(KeyString):
    KeyDict = {}

    KeyDict[0] = KeyString[0:4]
    KeyDict[1] = KeyString[4:8]
    KeyDict[2] = KeyString[8:12]
    KeyDict[3] = KeyString[12:16]

    return KeyDict

def readfile(name):
	#name= "text.txt"
	filehandle = open ( name, 'r' )
	str1 = filehandle.read()
	filehandle.close
	stringlist = list(str1)

	count = 0
	for y in stringlist:
		x = ord(y)
	
		if (x < 48 or x > 57) and (x < 65 or x > 90) and (x < 97 or x > 122):
			stringlist[count] = ""
		else:
			if (x > 96 and x < 123):
				stringlist[count] = stringlist[count].upper()
		count = count + 1


	str1 = "".join(stringlist)

	
	return str1


print "Enter the drive that the USB Key is mounted on"
Mount = raw_input()

OptionList = ['Encrypt', 'Decrypt', 'Marry', 'Quit']
print "This is the Dulwich College Raspberry Pi Encryption software."

loop = 0
pquit = 0
while pquit == 0:
    while loop == 0:
        Choice = MainMenu(OptionList)
        
        if Choice == 1:
            print("You chose to encrypt")
            print("Press 1 to confirm your choice")
            tempchoice = raw_input()
            tchoice = CheckIfInteger(tempchoice)
            if tchoice == 1:
                print ("Beginning encryption process")
                print (" ")
                print ("Before continuing, make sure you have placed the file in the same folder as the program")
                print ("")
                Filename = raw_input("Enter the name of the file, including the .txt extension:  ")
                Plaintext = readfile(Filename)
                Key = GetKey(Mount)
                NewKey = Encrypt.GenerateKey()
                NewKey = ConvertKeyToString(NewKey)
                StringToBeEncrypted = Plaintext + NewKey
                Ciphertext = Encrypt.ProcessString(StringToBeEncrypted, Key)
                FileWrite = "c" + Filename
                FileWrite = "EncryptedFiles/" + FileWrite
                EncryptionSuccess = Encrypt.PrintEncryption(Ciphertext, FileWrite)
                FileWriteSuccesful = WriteNewKey(Mount, (str(NewKey)))
                HashPS = Hasher.GetString(Ciphertext)
                HashP = Hasher.HashString(HashPS)
                HashWriteSuccessful = WriteHash(HashP, FileWrite)
                
                
                print "Encryption Successful!"               
                              
                loop = Continue()
                
            else:
                print(" ")
                loop = 0
            
            

        elif Choice == 2:
            print("You chose to get decrypt")
            print("Press 1 to confirm your choice")
            tempchoice = raw_input()
            tchoice = CheckIfInteger(tempchoice)
            if tchoice == 1:
                print ("Beginning decryption process")
                print (" ")
                print ("Before continuing, make sure you have placed the file in the 'EncryptedFiles' folder")
                print ("")
                CipherFileName = raw_input("Enter the name of the file, including the .txt extension: ")
                CipherTempFile = CipherFileName
                CipherFileName = "EncryptedFiles/" + CipherFileName        
                CipherHashList = ReadThisFile(CipherFileName)
                CipherText = NumericCipherList(CipherHashList[0])
                HashCS = Hasher.GetString(CipherText)
                HashC = Hasher.HashString(HashCS)
                if HashC == (CipherHashList[1]):
                    Key = GetKey(Mount)
                    Plaintext = Decryption.Decipher(CipherText, Key)
                    CipherLength = len(CipherText)
                    StringLength = (CipherLength/2)
                    if Plaintext[-1] == "Z":
                        NewKeyD = Plaintext[(StringLength-17):(StringLength-1)]
                        DecryptedText = Plaintext[0:(StringLength-17)]
                    else:
                        NewKeyD = Plaintext[(StringLength-16):StringLength]
                        DecryptedText = Plaintext[0:(StringLength-16)] 
                    NewKeyD = NewKeyD.lower()
                    NewKeyDict = ConvertToDictionary(NewKeyD)
                    NewKeyS = ConvertKeyToString(NewKeyDict)
                    FileWriteDSuccesful = WriteNewKey(Mount, NewKeyS)
                    
                    FileLocation = "EncryptedFiles/DECRYPTED" + CipherTempFile
                    PrintDecryption = PrintDecryptedText(DecryptedText, FileLocation)
                    
                    print "Decryption Successful!"
                    loop = Continue()
                else:
                    print "This messsage has been modified in some way!"
                    print "The message will be rejected"
                    
                    
                    
                
                
                loop = 1
            else:
                print(" ")
                loop = 0
            

        elif Choice == 3:
            print("You chose to pair programs")
            print("Press 1 to confirm your choice")
            tempchoice = raw_input()
            tchoice = CheckIfInteger(tempchoice)
            if tchoice == 1:
                print ("Beginning marrying process")
                Key = Marry()
                Key = ConvertKeyToString(Key)
                FileWriteMSuccessful = WriteNewKey(Mount, Key)
                loop = Continue()
            else:
                print(" ")
                loop = 0

        



        elif Choice == 4:
            print("You chose to quit")
            print("Press 1 to confirm your choice")
            tempchoice = raw_input()
            tchoice = CheckIfInteger(tempchoice)
            if tchoice == 1:
                print ("Quitting")
                loop = 1
            else:
                print(" ")
                loop = 0



                
        else:
            print("That option is not available, remember to pick the number not the word")
            print(" ")
            
     

