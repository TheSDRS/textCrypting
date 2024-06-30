import math
import random
import threading
import time

import numpy as np
import text

# getting the german word list file and open it to read
germanWords = open("germanWords.txt", "r")
# reading the content of the file aka getting every word
gerWords = germanWords.read()


# function to strip a given 'text input' from its " or '
def stripText(textToStrip: str):
    # just removing the characters
    if textToStrip.startswith("'") or textToStrip.startswith('"'):
        if textToStrip.endswith("'") or textToStrip.endswith('"'):
            textToStrip = textToStrip.removeprefix(textToStrip[0])
            textToStrip = textToStrip.removesuffix(textToStrip[len(textToStrip) - 1])
            return textToStrip


# function to generate a random upper case Cryptic key
def generateKey() -> list:
    # String with possible characters (upper case alphabet)
    possibleChars = text.getAlphabet("upper")
    key = ""
    # Looping through all characters
    for i in range(26):
        # getting a random character
        rndChar = random.choice(possibleChars)
        # doing this until the character isn't in the key
        while rndChar in key:
            rndChar = random.choice(possibleChars)
        # adding the character to the key
        key = key + rndChar
    # returning the generated key
    return key


# Function to generate a new encrypted alphabet
def genKeyOffset(offset: int):
    # Getting the alphabets
    tmpListL = text.getAlphabet("lower")

    # Looping 'offset' times
    for i in range(offset):

        # Getting current first letter in the half encrypted alphabet
        currentFirstLetterL = tmpListL[0]

        # Looping through the half encrypted alphabet
        for l in range(1, len(tmpListL)):

            # As 'l' is the current location in the alphabet Array we need to set the 'l - 1' letter to the 'l' letter
            tmpListL[l - 1] = tmpListL[l]

            # Checking if the 'l' letter is the last letter in the list
            if l == len(tmpListL) - 1:
                # Setting last letter to the earlier saved first letter
                tmpListL[l] = currentFirstLetterL

    # just making all letters upper case and adding them to the upper case list
    tmpListU = []
    for letter in tmpListL:
        tmpListU.append(letter.capitalize())

    # Returning the global encryption key lists
    return tmpListU, tmpListL


# this function calculates a score based on the words
def checkWords(text: str) -> float:
    # the score is calculated by checking if a word is in a large list of german words
    # for every word that is found the score is added +1
    # after every word is looked up 1 is divided by the score
    # then for style and ease of use the score is subtracted from 1
    score = 1
    # getting all words and adding them to a list
    words = text.split(" ")
    # looping through the words of the encrypted text
    for word in words:
        # if the word is found in the list of german words the score is adde +1
        if word in gerWords:
            score += 1
    # calculating the final score
    finalScore = 1 - (1 / score)
    # returning the final score
    return finalScore


# this function sorts a python dictionary from the highest score to lowest
def sortDict(dictionary: dict) -> dict:
    sortedDict = {}
    values = []
    # looping through all values in the dictionary
    for value in dictionary.values():
        # adding the value to the 'values' list
        values.append(value)

    # getting the numpy library to sort the values list
    npArray = np.array(values)
    sortedArray = np.sort(npArray, -1, "stable", None)

    # sorting the dictionary by getting the corresponding texts to the scores
    for i in range(len(sortedArray) - 1, 0, -1):
        for key in dictionary.keys():
            if dictionary[key] == sortedArray[i]:
                sortedDict[key] = sortedArray[i]

    # returning the sorted dictionary
    return sortedDict


# this function generates an output file
def genOutputFile(text: str, isEncrypted: bool):
    # printing some user feedback
    print("Generating output file...")
    # checking if the files content is encrypted
    if isEncrypted:
        # if yes
        # open a file with the name 'encryptedOutput.txt' for writing
        file = open("encryptedOutput.txt", "w")
        # writing the text to the file
        file.write(text)
        # closing the file so that it could be edited without errors
        file.close()
    else:
        # if not the file is 'decrypted'
        # open a file with the name 'decryptedOutput.txt' for writing
        file = open("decryptedOutput.txt", "w")
        # writing the text to the file
        file.write(text)
        # closing the file so that it could be edited without errors
        file.close()
    # printing some user feedback
    print("Output file generated!")


# this function prints all help you could get for this programme
def printHelp():
    # printing some user feedback
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
    print("'bruteforce' [EXPERIMENTAL]: ")
    print("     usage: bruteforce [textToBruteforce]")
    print("     action: tries to bruteforce-decrypt the given text")
    print("'help': prints this help text")


bestScore = 0.0
bestKey = ""
bestDecryptedText = ""


def bruteForceDecrypt(currentKey: str, currentLetter: str, textToDecrypt: str):
    global bestScore, bestKey, bestDecryptedText
    if text.isDecrypted.isSet():
        threading.current_thread().join()
    else:
        currentKey = currentKey + currentLetter
        if len(currentKey) == 26:
            text.cryptKeyU = []
            text.cryptKeyL = []
            for letter in currentKey:
                text.cryptKeyU.append(letter)
                text.cryptKeyL.append(letter.lower())
            decryptedText = text.decrypt(textToDecrypt)
            score = checkWords(decryptedText)
            text.triedCombinations.put(currentKey)
            if score > bestScore:
                bestScore = score
                bestKey = currentKey
                bestDecryptedText = decryptedText
                print("Current Key: " + str(currentKey) + ", Best Score: " + str(bestScore) + ", Decrypted Text: " + str(bestDecryptedText))
        else:
            for letter in text.getAlphabet("upper"):
                if letter not in currentKey:
                    thread = threading.Thread(target=bruteForceDecrypt, args=(currentKey, letter, textToDecrypt))
                    thread.start()
                    thread.join()


def countThreads(arg: str):
    t1 = math.floor(time.time())
    prvDiff = 0
    diff = 0
    while True:
        t = math.floor(time.time() - t1)
        if not t == prvDiff:
            prvDiff = t
            diff += 1
        if diff == 60:
            print("Time in Seconds: " + str(t) + ", Thread Count: " + str(threading.active_count())
                  + ", Tried Combinations: " + str(text.triedCombinations.qsize()))
            diff = 0
