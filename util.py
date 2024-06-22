import random
import numpy as np


def stripText(textToStrip: str):
    if textToStrip.startswith("'") or textToStrip.startswith('"'):
        if textToStrip.endswith("'") or textToStrip.endswith('"'):
            textToStrip = textToStrip.removeprefix(textToStrip[0])
            textToStrip = textToStrip.removesuffix(textToStrip[len(textToStrip) - 1])
            return textToStrip


def generateKey() -> list:
    possibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""
    for i in range(26):
        rndChar = random.choice(possibleChars)
        while rndChar in key:
            rndChar = random.choice(possibleChars)
        key = key + rndChar
    return key


def checkWords(text: str) -> float:
    score = 1
    words = text.split(" ")
    germanWords = open("germanWords.txt", "r")
    gerWords = germanWords.read()
    for word in words:
        if word in gerWords:
            score += 1
    finalScore = 1 - (1 / score)
    return finalScore


def sortDict(dictionary: dict) -> dict:
    sortedDict = {}
    values = []
    for value in dictionary.values():
        values.append(value)

    npArray = np.array(values)
    sortedArray = np.sort(npArray, -1, "stable", None)

    for i in range(len(sortedArray) - 1, 0, -1):
        for key in dictionary.keys():
            if dictionary[key] == sortedArray[i]:
                sortedDict[key] = sortedArray[i]

    return sortedDict


def genOutputFile(text: str, isEncrypted: bool):
    print("Generating output file...")
    if isEncrypted:
        file = open("encryptedOutput.txt", "w")
        file.write(text)
        file.close()
    else:
        file = open("decryptedOutput.txt", "w")
        file.write(text)
        file.close()
    print("Output file generated!")


def printHelp():
    print("'exit': exit the program")
    print("'encrypt': ")
    print("     usage: encrypt [text|file] [textToEncrypt|fileToEncrypt]")
    print("     action: encrypts the given text or file")
    print("'setkey': ")
    print("     usage: setkey [offset|custom] [offset|customKey]")
    print("     action: set's the encryption and decryption keys")
    print("'decrypt': ")
    print("     usage: decrypt [text|file] [textToDecrypt|fileToDecrypt] -a")
    print("     action: decrypts the given text or file")
    print("'getkeys': returns the current  encryption and decryption keys")
    print("'generatekey': Generates a new Cryptic Key with upper and lower letters")
    print("'help': prints this help text")
