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
        # when the 'encrypt' command is called the sub handler function 'encrypt' is called
        # to make things easier the first argument gets removed beforehand
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
    elif cmd.startswith("generatekey"):
        print("Generated new Cryptic Key: \n" + str(util.generateKey()))
    elif cmd.startswith("help"):
        util.printHelp()
    else:
        util.printHelp()


def encrypt(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt [args]'")
    else:
        args = args.removeprefix(" ")
        if args.startswith("text"):
            args = args.removeprefix("text")
            encryptText(args)
        elif args.startswith("file"):
            args = args.removeprefix("file")
            encryptFile(args)


def encryptText(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt text [text]'")
    else:
        args = args.removeprefix(" ")
        textToEncrypt = util.stripText(args)
        encryptedText = text.encrypt(textToEncrypt)
        util.genOutputFile(encryptedText, True)
        print("Encrypted Text: \n" + encryptedText)


def encryptFile(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'encrypt file [Path to file]'")
    else:
        args = args.removeprefix(" ")
        filePath = util.stripText(args)
        file = open(filePath, "r")
        textToEncrypt = file.read()
        encryptedText = text.encrypt(textToEncrypt)
        util.genOutputFile(encryptedText, True)
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
        text.genCrypticKey(int(args))
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
        if args.endswith("-a"):
            args = args.removesuffix(" -a")
            textToDecrypt = util.stripText(args)
            options = text.decryptAuto(textToDecrypt)
            print("Tried to decrypt: \n")
            i = 1
            for key in options.keys():
                if i < 2:
                    util.genOutputFile(key, False)
                    print(key)
                else:
                    break

        else:
            textToDecrypt = util.stripText(args)
            decryptedText = text.decrypt(textToDecrypt)
            util.genOutputFile(decryptedText, False)
            print("Decrypted text: \n" + decryptedText)


def decryptFile(args: str):
    if args == "" or args is None or len(args) == 0:
        print("Please use 'decrypt file [Path to file]'")
    else:
        args = args.removeprefix(" ")
        if args.endswith("-a"):
            args = args.removesuffix(" -a")
            filePath = util.stripText(args)
            file = open(filePath, "r")
            textToDecrypt = file.read()
            options = text.decryptAuto(textToDecrypt)
            print("Tried to decrypt: \n")
            i = 1
            for key in options.keys():
                if i < 2:
                    util.genOutputFile(key, False)
                    print(key)
                    i += 1
        else:
            filePath = util.stripText(args)
            file = open(filePath, "r")
            textToDecrypt = file.read()
            decryptedText = text.decrypt(textToDecrypt)
            util.genOutputFile(decryptedText, False)
            print("Decrypted text: \n" + decryptedText)
