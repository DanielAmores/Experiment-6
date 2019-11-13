def isWordGuessed(secretWord,lettersGuessed):
    for a in lettersGuessed:
        if a not in secretWord:
            return False
    for a in secretWord:
        if a not in lettersGuessed:
            return False
    return True
