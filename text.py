import string

alphabetL = string.ascii_uppercase
alphabetS = string.ascii_lowercase

def getAlphabet(case:str):
    if case == "lower":
        return alphabetS
    if case == "upper":
        return alphabetL
    else:
        return