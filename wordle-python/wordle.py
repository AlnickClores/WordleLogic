import random
from wordleWords import words

chances = 5
wordleWord = random.choice(words).lower()
guessWord = ''

print(wordleWord)

def checkWordle(guessWord, wordleWord):
    correctLetters = []
    correctPositions = []

    for i, letter in enumerate(guessWord):
        if letter in wordleWord:
            correctLetters.append(letter)
        if letter == wordleWord[i]:
            correctPositions.append(letter)
    
    print("Correct letters: ", correctLetters)
    print("Correct positions: ", correctPositions)

    return guessWord == wordleWord

def gameOver(chances):
    if chances == 0:
        print("Game Over")

while chances > 0:
    guessWord = input('Enter your guess word: ')
    guessWord = guessWord.lower()
    if len(guessWord) != len(wordleWord):
        print(f"Please enter a {len(wordleWord)}-letter word.")
        continue

    if checkWordle(guessWord, wordleWord):
        print("You've guessed it right!")
        break
    else:
        chances -= 1
        print(f"Wrong, please try again. You have {chances} chances left.")
        gameOver(chances)

if chances == 0:
    print(f"The correct word was '{wordleWord}'. Better luck next time!")
