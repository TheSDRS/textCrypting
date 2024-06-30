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
    # getting some variables
    global bestScore, bestKey, bestDecryptedText
    # checking if some other thread found the right combination
    if text.isDecrypted.isSet():
        # closing current thread
        threading.current_thread().join()
    else:
        # adding the current letter to the current key
        currentKey = currentKey + currentLetter
        # checking if the currentKey is finished
        if len(currentKey) == 26:
            # setting the cryptik keys up for decrypting
            text.cryptKeyU = []
            text.cryptKeyL = []
            for letter in currentKey:
                text.cryptKeyU.append(letter)
                text.cryptKeyL.append(letter.lower())
            # decrypting the text
            decryptedText = text.decrypt(textToDecrypt)
            # generating a score based on the result
            score = checkWords(decryptedText)
            # adding the current combination to a shared list
            text.triedCombinations.put(currentKey)
            # checking if the calculated score is an improvement
            if score > bestScore:
                # setting the best score to the current score
                bestScore = score
                # setting the best key to the current key
                bestKey = currentKey
                # setting the best decrypted tex to the current decrypted text
                bestDecryptedText = decryptedText
                # printing some user feedback
                print("Current Key: " + str(currentKey) + ", Best Score: " + str(bestScore) + ", Decrypted Text: " + str(bestDecryptedText))
        else:
            # looping through the upper case alphabet
            for letter in text.getAlphabet("upper"):
                # checking if letter is already in the current key
                if letter not in currentKey:
                    # creating a new thread with this function
                    thread = threading.Thread(target=bruteForceDecrypt, args=(currentKey, letter, textToDecrypt))
                    # running the thread
                    thread.start()
                    # if the thread finishes it gets joined into the main thread if I understood this correctly
                    thread.join()


# function for counting time and threads
def countThreads(arg: str):
    # getting the current time in seconds
    t1 = math.floor(time.time())
    prvDiff = 0
    diff = 0
    # looping as long the application/thread is running
    while True:
        # getting the time difference
        t = math.floor(time.time() - t1)
        # checking if the current time in seconds is the previous time
        if not t == prvDiff:
            # setting the previous difference to the current difference
            prvDiff = t
            # adding one to the difference variable
            diff += 1
        # checking if the difference variable is 60 aka waiting 60 seconds
        if diff == 60:
            # printing some user feedback
            # like the current time it took and the current thread count and tried combinations
            print("Time in Seconds: " + str(t) + ", Thread Count: " + str(threading.active_count())
                  + ", Tried Combinations: " + str(text.triedCombinations.qsize()))
            # resetting the difference Variable
            diff = 0
