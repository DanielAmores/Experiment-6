def getAvailableLetters(lettersGuessed):
    import string
    a = string.ascii_lowercase
    b = ''
    for x in a:
        if x not in lettersGuessed:
            b = b + x
    return b