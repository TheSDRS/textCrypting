cryptAlphaL = []
cryptAlphaS = []

def getAlphabet(case:str):
    alphabetL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabetS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    if case == "lower":
        return alphabetS
    if case == "upper":
        return alphabetL
    else:
        return

def genCryptikKey(offset:int):
    tmpListL = getAlphabet("upper")
    tmpListS = getAlphabet("lower")
    for i in range(offset):
        tmpLetter = tmpListL[0]
        for l in range(1 ,len(tmpListL)):
            tmpListL[l - 1] = tmpListL[l]
            if l == len(tmpListL) - 1:
                tmpListL[l] = tmpLetter