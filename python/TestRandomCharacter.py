import RandomCharacter

number_of_chars = 96
chars_per_line = 24
for i in range(number_of_chars):
    #print(RandomCharacter.getRandomLowerCaseLetter(),end = "")
    print(RandomCharacter.getRandomASCIILetter(),end = "")

    if (i+1) % chars_per_line == 0:
        print()
