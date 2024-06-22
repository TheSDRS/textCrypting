import util

cryptKeyU = []
cryptKeyL = []


# Function to get the UpperCase or LowerCase Alphabet
# Could have used the String Library but didn't because of SCHOOL
def getAlphabet(case: str) -> str:
    alphabetL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    alphabetS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    if case == "lower":
        return alphabetS
    if case == "upper":
        return alphabetL
    else:
        return


# Function to generate a new encrypted alphabet
def genCrypticKey(offset: int):
    # Getting the alphabets
    tmpListL = getAlphabet("lower")

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

    # Setting the global encryption key lists
    global cryptKeyU
    global cryptKeyL
    cryptKeyU = tmpListU
    cryptKeyL = tmpListL


def encrypt(plainText: str) -> str:
    encryptedText = ""

    for letter in plainText:
        if letter in cryptKeyU:
            encryptedText = encryptedText + cryptKeyU[getAlphabet("upper").index(letter)]
        elif letter in cryptKeyL:
            encryptedText = encryptedText + cryptKeyL[getAlphabet("lower").index(letter)]
        else:
            encryptedText = encryptedText + letter

    return encryptedText


def decrypt(encryptedText: str) -> str:
    decryptedText = ""

    for letter in encryptedText:
        if letter in getAlphabet("upper"):
            decryptedText = decryptedText + getAlphabet("upper")[cryptKeyU.index(letter)]
        elif letter in getAlphabet("lower"):
            decryptedText = decryptedText + getAlphabet("lower")[cryptKeyL.index(letter)]
        else:
            decryptedText = decryptedText + letter

    return decryptedText


def decryptAuto(encryptedText: str) -> dict:
    decryptionOptions = []
    for i in range(1, 26):
        genCrypticKey(i)
        decryptionOptions.append(decrypt(encryptedText))

    scores = []
    for text in decryptionOptions:
        scores.append(util.checkWords(text))

    optionDictionary = {}
    for i in range(0, 25):
        optionDictionary[decryptionOptions[i]] = scores[i]

    return util.sortDict(optionDictionary)
