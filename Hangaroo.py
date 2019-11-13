def isWordGuessed(secretWord,lettersGuessed):
    for a in lettersGuessed:
        if a not in secretWord:
            return False
    for a in secretWord:
        if a not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    a = ""
    for letters in secretWord:
        if letters in lettersGuessed:
            a += letters
        elif letters not in lettersGuessed:
            a += "_"
    return a

def getAvailableLetters(lettersGuessed):
    import string
    a = string.ascii_lowercase
    b = ''
    for x in a:
        if x not in lettersGuessed:
            b = b + x
    return b

def Hangaroo(secretWord):
    print("Welcome to Hangaroo! You only have 8 guesses.")
    lettersGuessed = ''
    availLetters = getAvailableLetters(lettersGuessed)        
    tries = 8
    while tries > 0:
        print()
        print("Secret Word : " + getGuessedWord(secretWord,lettersGuessed))
        letter = input("Guess a letter : ")
        if letter not in availLetters:
            print("You already used that letter.")
        else:
            if letter not in secretWord:
                print("Wrong letter")
            else:
                lettersGuessed += letter
                availLetters = getAvailableLetters(lettersGuessed)        
        if isWordGuessed(secretWord,lettersGuessed):
            print("Word : " + getGuessedWord(secretWord,lettersGuessed))
            print("Good Job! You guessed the secret word")
            return
        tries -= 1
        print("Remaining tries : ", + tries)
    else:
        if tries == 0:
            print("Sorry, no more tries")
               
        
    return



