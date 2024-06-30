import threading
from multiprocessing import Queue

import util

cryptKeyU = []
cryptKeyL = []


# Function to get the UpperCase or LowerCase Alphabet
# Could have used the String Library but didn't because of SCHOOL
def getAlphabet(case: str) -> str:
    # upper case alphabet
    alphabetU = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    # lower case alphabet
    alphabetL = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    # checking which alphabet to return
    if case == "lower":
        return alphabetL
    if case == "upper":
        return alphabetU
    else:
        return


# Function to generate a new encrypted alphabet
def genCrypticKey(offset: int):
    # Setting the global encryption key lists
    global cryptKeyU
    global cryptKeyL
    cryptKeyU, cryptKeyL = util.genKeyOffset(offset)


# function to encrypt the given text with the given Cryptic key
def encrypt(plainText: str) -> str:
    encryptedText = ""

    # looping through every letter in the given text
    for letter in plainText:
        # checking if the letter is upper-/ lower case or is even an encrypt able letter
        if letter in cryptKeyU:
            # if the letter is upper case
            # get the index of the letter in the alphabet
            # then get the corresponding letter at the Cryptic key and add it to the encrypted text
            encryptedText = encryptedText + cryptKeyU[getAlphabet("upper").index(letter)]
        elif letter in cryptKeyL:
            # if the letter is lower case
            # get the index of the letter in the alphabet
            # then get the corresponding letter at the Cryptic key and add it to the encrypted text
            encryptedText = encryptedText + cryptKeyL[getAlphabet("lower").index(letter)]
        else:
            # if the letter isn't in both of the alphabets the letter is 'not encrypt able'
            # just adding the letter to the encrypted text
            encryptedText = encryptedText + letter

    # returning the fully encrypted text
    return encryptedText


# this function decrypts the given text with the given Cryptic key
def decrypt(encryptedText: str) -> str:
    decryptedText = ""

    # looping through every letter in the encrypted text
    for letter in encryptedText:
        # checking if the letter is upper-/ lower case or is even a decrypt able letter
        if letter in getAlphabet("upper"):
            # if the letter is upper case
            # get the index of the letter in the Cryptic key
            # then get the corresponding letter at the alphabet and add it to the decrypted text
            decryptedText = decryptedText + getAlphabet("upper")[cryptKeyU.index(letter)]
        elif letter in getAlphabet("lower"):
            # if the letter is lower case
            # get the index of the letter in the Cryptic key
            # then get the corresponding letter at the alphabet and add it to the decrypted text
            decryptedText = decryptedText + getAlphabet("lower")[cryptKeyL.index(letter)]
        else:
            # if the letter isn't in both of the Cryptic keys the letter is 'not decrypt able'
            # just adding the letter to the decrypted text
            decryptedText = decryptedText + letter

    # returning the fully decrypted text
    return decryptedText


# this function tries to decrypt a given text without a Cryptic key
def decryptAuto(encryptedText: str) -> dict:
    decryptionOptions = []
    # looping alphabet length times
    for i in range(1, 26):
        # for each value for 'i' a new Cryptic offset key is generated
        genCrypticKey(i)
        # adding the 'decrypted' text to the 'decryptionOptions' list
        decryptionOptions.append(decrypt(encryptedText))

    # looping through every text in the options list
    scores = []
    for text in decryptionOptions:
        # calculating a score of how good the text is decrypted and adding the score to the 'scores' list
        scores.append(util.checkWords(text))

    # looping through every option
    optionDictionary = {}
    for i in range(0, 25):
        # adding every option text with its corresponding score to the dictionary
        optionDictionary[decryptionOptions[i]] = scores[i]

    # returning a sorted dictionary with the 'best' text on the first index
    return util.sortDict(optionDictionary)


isDecrypted = threading.Event()
triedCombinations = Queue()


def decryptBruteForce(encryptedText: str):
    counter = threading.Thread(target=util.countThreads, args=("lol",))
    counter.start()

    for letter in getAlphabet("upper"):
        thread = threading.Thread(target=util.bruteForceDecrypt, args=("", letter, encryptedText))
        thread.start()
        thread.join()

    counter.join()
