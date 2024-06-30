import os.path
import sys

import text
import util


def waitForInput():
    # cmd is the command th user entered with all arguments
    cmd = input("Please enter command (case lower): ")

    # managing witch command does what
    if cmd == "exit":
        # using the 'sys' library to exit the programme
        sys.exit()
    elif cmd.startswith("encrypt"):
        # when the 'encrypt' command is called the sub handler function 'encrypt()' is called
        # to make things easier the first argument gets removed beforehand
        args = cmd.removeprefix("encrypt")
        encrypt(args)
    elif cmd.startswith("setkey"):
        # when the 'setkey' command is called the sub handler function 'setKey()' is called
        # to make things easier the first argument gets removed beforehand
        args = cmd.removeprefix("setkey")
        setKey(args)
    elif cmd.startswith("decrypt"):
        # when the 'decrypt' command is called the sub handler function 'decrypt()' is called
        # to make things easier the first argument gets removed beforehand
        args = cmd.removeprefix("decrypt")
        decrypt(args)
    elif cmd.startswith("getkeys"):
        # printing the generated Cryptic keys that are currently loaded
        print("Cryptic key upper: " + str(text.cryptKeyU))
        print("Cryptic key lower: " + str(text.cryptKeyL))
    elif cmd.startswith("generatekey"):
        # just printing a randomly generated key from the util class
        print("Generated new Cryptic Key: \n" + str(util.generateKey()))
    elif cmd.startswith("bruteforce"):
        args = cmd.removeprefix("bruteforce")
        # when the 'bruteforce' command is called the sub handler function 'bruteForceDecrypt()' is called
        # to make things easier the first argument gets removed beforehand
        bruteForceDecrypt(args)
    elif cmd.startswith("help"):
        # for ease of use I'm calling a separate function to print the help things
        util.printHelp()
    else:
        util.printHelp()


# this function manages all arguments with the 'encrypt' command
def encrypt(args: str):
    # checking if the command is executed with arguments
    if args == "" or args is None or len(args) == 0:
        # printing a little bit of help when no arguments are found
        print("Please use 'encrypt [args]'")
    else:
        # handling the sub commands
        args = args.removeprefix(" ")
        if args.startswith("text"):
            # calling the text encryption function 'encryptText()'
            args = args.removeprefix("text")
            encryptText(args)
        elif args.startswith("file"):
            # calling the file encryption function 'encryptFile()'
            args = args.removeprefix("file")
            encryptFile(args)


# this function manages the encryption process of a text
def encryptText(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt text [text]'")
    else:
        args = args.removeprefix(" ")
        # getting the text that should get encrypted
        textToEncrypt = util.stripText(args)
        # encrypting the given text with the current Cryptic key
        encryptedText = text.encrypt(textToEncrypt)
        # generating an output file to save the last bit of progress
        util.genOutputFile(encryptedText, True)
        # printing the encrypted text for smaller texts and ease of use
        print("Encrypted Text: \n" + encryptedText)


# this function manages the encryption process of a file
def encryptFile(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt file [Path to file]'")
    else:
        args = args.removeprefix(" ")
        # getting the file path to the File that should be encrypted
        filePath = util.stripText(args)
        # checking if the file exists
        if os.path.isfile(filePath):
            # if file exist open the file to read
            file = open(filePath, "r")
            # reading the content of the file
            textToEncrypt = file.read()
            # encrypting the given text from the file with the current Cryptic key
            encryptedText = text.encrypt(textToEncrypt)
            # generating the output file to get a readable text mainly for longer texts
            util.genOutputFile(encryptedText, True)
            # printing the encrypted text for the user as feedback that something happened
            print("Encrypted Text: \n" + encryptedText)
        else:
            # if the file isn't found print an error
            print("File " + filePath + " was not found.")


# this function manages all arguments of the 'setkey' command
def setKey(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey [args]'")
    else:
        # handling the sub commands
        args = args.removeprefix(" ")
        if args.startswith("custom"):
            # calling the function to manage custom Cryptic keys 'setKeyCustom()'
            args = args.removeprefix("custom")
            setKeyCustom(args)
        elif args.startswith("offset"):
            # calling the function to set Cryptic keys with an offset 'setKeyOffset()'
            args = args.removeprefix("offset")
            setKeyOffset(args)


# this function manages the custom key calls
def setKeyCustom(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey custom [args]'")
    else:
        # handling sub commands
        args = args.removeprefix(" ")
        if args.startswith("upper"):
            # calling the function to set the custom key for Upper case 'setKeyCustomUpper()'
            args = args.removeprefix("upper")
            setKeyCustomUpper(args)
        elif args.startswith("lower"):
            # calling the function to set the custom key for Lower case 'setKeyCustomLower()'
            args = args.removeprefix("lower")
            setKeyCustomLower(args)


# this function manages setting the upper case custom keys
def setKeyCustomUpper(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey custom upper [key]'")
    else:
        args = args.removeprefix(" ")
        # getting the key that the user input
        key = util.stripText(args)
        # resetting the Cryptic key
        text.cryptKeyU = []
        # looping through the input
        for letter in key:
            # adding each letter to the Cryptic key
            text.cryptKeyU.append(letter)
        # printing some user feedback
        print("set new Cryptic key for upper: " + str(text.cryptKeyU))


# this function manages setting the lower case custom keys
def setKeyCustomLower(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey custom lower [key]'")
    else:
        args = args.removeprefix(" ")
        # getting the key that the user input
        key = util.stripText(args)
        # resetting the Cryptic key
        text.cryptKeyL = []
        # looping through the input
        for letter in key:
            # adding each letter to the Cryptic key
            text.cryptKeyL.append(letter)
        # printing some user feedback
        print("set new Cryptic key for lower: " + str(text.cryptKeyL))


# this function manages setting a Cryptic key with an offset
def setKeyOffset(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey offset [offset]'")
    else:
        args = args.removeprefix(" ")
        # generating the Cryptic key with the given offset
        # because the function sets a global variable we don't need to change the variable later
        text.genCrypticKey(int(args))
        # printing some user feedback
        print("generated an Cryptic key with an offset of '" + args + "'")
        print("Cryptic key upper: " + str(text.cryptKeyU))
        print("Cryptic key lower: " + str(text.cryptKeyL))


# this function manages all arguments with the 'decrypt' command
def decrypt(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt [args]'")
    else:
        # handling the sub commands
        args = args.removeprefix(" ")
        if args.startswith("text"):
            # calling the function 'decryptText()' to decrypt the given text
            args = args.removeprefix("text")
            decryptText(args)
        elif args.startswith("file"):
            # calling the function 'decryptFile()' to decrypt the given file
            args = args.removeprefix("file")
            decryptFile(args)


# this function manages decrypting texts
def decryptText(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt text [text]'")
    else:
        args = args.removeprefix(" ")
        # checking if the programme should try to decrypt the text without a given key
        if args.endswith("-a"):
            # if yes
            args = args.removesuffix(" -a")
            # getting the text to decrypt
            textToDecrypt = util.stripText(args)
            # letting the programme do it's magic and try to decrypt the text
            options = text.decryptAuto(textToDecrypt)
            # printing some user feedback
            print("Tried to decrypt: \n")
            # looping though the returned dictionary
            # not beautiful but it works
            i = 1
            for key in options.keys():
                if i < 2:
                    # generating the output file with the hopefully correctly decrypted text
                    util.genOutputFile(key, False)
                    # printing some more user feedback
                    print(key)
                else:
                    break
        else:
            # if the 'auto' mode isn't activated
            # getting the text to decrypt
            textToDecrypt = util.stripText(args)
            # decrypting the given text with the given Cryptic key
            decryptedText = text.decrypt(textToDecrypt)
            # generating the output file with the decrypted text
            util.genOutputFile(decryptedText, False)
            # printing some user feedback
            print("Decrypted text: \n" + decryptedText)


# this function manages decrypting files
def decryptFile(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt file [Path to file]'")
    else:
        # if yes
        args = args.removeprefix(" ")
        # checking if the programme should try to decrypt the file without a given key
        if args.endswith("-a"):
            args = args.removesuffix(" -a")
            # getting the file path of the file to decrypt
            filePath = util.stripText(args)
            # checking if the given file exist
            if os.path.isfile(filePath):
                # if it does open it to read
                file = open(filePath, "r")
                # reading the content of the file
                textToDecrypt = file.read()
                # letting the programme do it's magic and try to decrypt the text
                options = text.decryptAuto(textToDecrypt)
                # printing some user feedback
                print("Tried to decrypt: \n")
                # looping though the returned dictionary
                # not beautiful but it works
                i = 1
                for key in options.keys():
                    if i < 2:
                        # generating the output file with the hopefully correctly decrypted text
                        util.genOutputFile(key, False)
                        # printing some more user feedback
                        print(key)
                    i += 1
            else:
                # if not print an error
                print("File " + filePath + " was not found.")
        else:
            # if the 'auto' mode isn't activated
            # getting the given file path
            filePath = util.stripText(args)
            # checking if the file exists
            if os.path.isfile(filePath):
                # if yes
                # open the file to read
                file = open(filePath, "r")
                # reading the content of the file
                textToDecrypt = file.read()
                # decrypting the given text with the given Cryptic key
                decryptedText = text.decrypt(textToDecrypt)
                # generating the output file with the decrypted text
                util.genOutputFile(decryptedText, False)
                # printing some user feedback
                print("Decrypted text: \n" + decryptedText)
            else:
                # if not print an error
                print("File " + filePath + " was not found.")


# this function manages the bruteForce command
def bruteForceDecrypt(args: str):
    # checking for arguments
    if args == "" or args is None or len(args) == 0:
        # printing some user feedback
        print("Please use 'bruteforce [text]'")
    else:
        # removing some useless char
        args = args.removeprefix(" ")
        # getting the text to decrypt
        textToDecrypt = util.stripText(args)
        # printing some more user feedback
        print("Brute forcing decryption of '" + textToDecrypt + "'")

        # attempting brute forcing the text
        text.decryptBruteForce(textToDecrypt)
