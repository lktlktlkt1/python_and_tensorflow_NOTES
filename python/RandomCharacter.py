from random import randint
def getRandomCharacter(ch1,ch2):
    return chr(randint(ord(ch1),ord(ch2)))
def getRandomLowerCaseLetter():
    return getRandomCharacter("a","z")
def getRandomUpperCaseLetter():
    return getRandomCharacter("A","Z")
def getRandomDIgitLetter():
    return getRandomCharacter("0","9")
def getRandomASCIILetter():
    return chr(randint(0,127))