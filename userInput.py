import sys

import text
import util


def waitForInput():
    cmd = input("Please enter command (case lower): ")

    if cmd == "exit":
        sys.exit()
    elif cmd.startswith("encrypt"):
        args = cmd.removeprefix("encrypt")
        encrypt(args)
    elif cmd.startswith("setkey"):
        args = cmd.removeprefix("setkey")
        setKey(args)
    elif cmd.startswith("decrypt"):
        args = cmd.removeprefix("decrypt")
        decrypt(args)
    elif cmd.startswith("getkeys"):
        print("Cryptic key upper: " + str(text.cryptKeyU))
        print("Cryptic key lower: " + str(text.cryptKeyL))
    elif cmd.startswith("help"):
        print("'exit': exit the program")
        print("'encrypt': ")
        print("     usage: encrypt [text|file] [textToEncrypt|fileToEncrypt]")
        print("     action: encrypts the given text or file")
        print("'setkey': ")
        print("     usage: setkey [offset|custom] [offset|customKey]")
        print("     action: set's the encryption and decryption keys")
        print("'decrypt': ")
        print("     usage: decrypt [text|file] [textToDecrypt|fileToDecrypt]")
        print("     action: decrypts the given text or file")
        print("'getkeys': returns the current  encryption and decryption keys")
        print("'help': prints this help text")


def encrypt(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt [args]'")
    else:
        args = args.removeprefix(" ")
        if args.startswith("text"):
            args = args.removeprefix("text")
            caesarText(args)
        elif args.startswith("file"):
            args = args.removeprefix("file")
            caesarFile(args)


def caesarText(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt caesar text [text]'")
    else:
        args = args.removeprefix(" ")
        textToEncrypt = util.stripText(args)
        print("Encrypted Text: \n" + text.encryptCaesar(textToEncrypt))


def caesarFile(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt caesar file [Path to file]'")
    else:
        args = args.removeprefix(" ")
        filePath = util.stripText(args)
        file = open(filePath, "r")
        textToEncrypt = file.read()
        encryptedText = text.encryptCaesar(textToEncrypt)
        encryptedFile = open("outputEncrypted.txt", "w")
        encryptedFile.write(encryptedText)
        print("Encrypted Text: \n" + encryptedText)


def setKey(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey [args]'")
    else:
        args = args.removeprefix(" ")
        if args.startswith("custom"):
            args = args.removeprefix("custom")
            setKeyCustom(args)
        elif args.startswith("offset"):
            args = args.removeprefix("offset")
            setKeyOffset(args)


def setKeyCustom(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey custom [args]'")
    else:
        args = args.removeprefix(" ")
        if args.startswith("upper"):
            args = args.removeprefix("upper")
            setKeyCustomUpper(args)

        elif args.startswith("lower"):
            args = args.removeprefix("lower")
            setKeyCustomLower(args)


def setKeyCustomUpper(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey custom upper [key]'")
    else:
        args = args.removeprefix(" ")
        key = util.stripText(args)
        text.cryptKeyU = []
        for letter in key:
            text.cryptKeyU.append(letter)
        print("set new Cryptic key for upper: " + str(text.cryptKeyU))


def setKeyCustomLower(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey custom lower [key]'")
    else:
        args = args.removeprefix(" ")
        key = util.stripText(args)
        text.cryptKeyL = []
        for letter in key:
            text.cryptKeyL.append(letter)
        print("set new Cryptic key for lower: " + str(text.cryptKeyL))


def setKeyOffset(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'setkey offset [offset]'")
    else:
        args = args.removeprefix(" ")
        text.genCryptikKey(int(args))
        print("generated an Cryptic key with an offset of '" + args + "'")
        print("Cryptic key upper: " + str(text.cryptKeyU))
        print("Cryptic key lower: " + str(text.cryptKeyL))


def decrypt(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt [args]'")
    else:
        args = args.removeprefix(" ")
        if args.startswith("text"):
            args = args.removeprefix("text")
            decryptText(args)
        elif args.startswith("file"):
            args = args.removeprefix("file")
            decryptFile(args)


def decryptText(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt text [text]'")
    else:
        args = args.removeprefix(" ")
        textToDecrypt = util.stripText(args)
        decryptedText = text.decryptCaesar(textToDecrypt)
        print("Decrypted text: \n" + decryptedText)


def decryptFile(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt file [Path to file]'")
    else:
        args = args.removeprefix(" ")
        filePath = util.stripText(args)
        file = open(filePath, "r")
        textToDecrypt = file.read()
        decryptedText = text.decryptCaesar(textToDecrypt)
        decryptedFile = open("outputDecrypted.txt", "w")
        decryptedFile.write(decryptedText)
        print("Decrypted text: \n" + decryptedText)
