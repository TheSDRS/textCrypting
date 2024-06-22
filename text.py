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
def genCryptikKey(offset: int):
    # Getting the alphabets
    tmpListL = getAlphabet("upper")
    tmpListS = getAlphabet("lower")

    # Looping 'offset' times
    for i in range(offset):

        # Getting current first letter in the half encrypted alphabet
        currentFirstLetterL = tmpListL[0]
        currentFirstLetterS = tmpListS[0]

        # Looping through the half encrypted alphabet
        for l in range(1, len(tmpListL)):

            # As 'l' is the current location in the alphabet Array we need to set the 'l - 1' letter to the 'l' letter
            tmpListL[l - 1] = tmpListL[l]
            tmpListS[l - 1] = tmpListS[l]

            # Checking if the 'l' letter is the last letter in the list
            if l == len(tmpListL) - 1:
                # Setting last letter to the earlier saved first letter
                tmpListL[l] = currentFirstLetterL
                tmpListS[l] = currentFirstLetterS

    # Setting the global encryption key lists
    global cryptKeyU
    global cryptKeyL
    cryptKeyU = tmpListL
    cryptKeyL = tmpListS


def encryptCaesar(plainText: str) -> str:
    encryptedText = ""

    for letter in plainText:
        if letter in cryptKeyU:
            encryptedText = encryptedText + cryptKeyU[getAlphabet("upper").index(letter)]
        elif letter in cryptKeyL:
            encryptedText = encryptedText + cryptKeyL[getAlphabet("lower").index(letter)]
        else:
            encryptedText = encryptedText + letter

    return encryptedText


def decryptCaesar(encryptedText: str) -> str:
    decryptedText = ""

    for letter in encryptedText:
        if letter in getAlphabet("upper"):
            decryptedText = decryptedText + getAlphabet("upper")[cryptKeyU.index(letter)]
        elif letter in getAlphabet("lower"):
            decryptedText = decryptedText + getAlphabet("lower")[cryptKeyL.index(letter)]
        else:
            decryptedText = decryptedText + letter

    return decryptedText
