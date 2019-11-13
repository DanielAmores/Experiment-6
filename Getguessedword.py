def getGuessedWord(secretWord, lettersGuessed):
    a = ""
    for letters in secretWord:
        if letters in lettersGuessed:
            a += letters
        elif letters not in lettersGuessed:
            a += "_"
    return a