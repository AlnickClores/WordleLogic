chances = 5
wordleWord = 'thank'
guessWord = ''

def checkWordle():
  correctLetters = []

  if wordleWord == guessWord:
    return True
  
  for letter in guessWord:
    if letter in wordleWord:
      correctLetters.append(letter)

  print(correctLetters)

def gameOver(chances):
  if chances == 0:
      print("Game Over")

while chances > 0:
  guessWord = input('Enter your guess word: ')
  checkWordle()

  if guessWord == wordleWord:
    print("You've guessed it right!")
    break
  else:
    chances -= 1
    print("Wrong, please try again.")
    gameOver(chances)

