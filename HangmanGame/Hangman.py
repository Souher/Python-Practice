alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

GuessedLetters = []

WrongLetters = []

Words = ["beams", "irate", "reinhardt", "develop", "python"]

import random
Word = random.choice(Words)

Answer = []

def set_answer():
  global Word
  global Answer
  
  for letter in Word:
    Answer.append("_")

Count = 6

CorrectGuess = 0

global IsPresent 
IsPresent = False

def reset_alphabet():
  global alphabet
  ResetAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  alphabet = list(ResetAlphabet)

def check_if_letter_is_present(guess):
    for letter in GuessedLetters:
     if guess == letter:
        global IsPresent
        IsPresent = True

def letter_is_wrong(guess):
    global alphabet
    GuessedLetters.append(guess)
    WrongLetters.append(guess)
    alphabet.remove(guess)
    global Count 
    Count -= 1
    print(f"Wrong choice you have {Count} tries left")

def letter_is_correct(guess):
    global Word
    global CorrectGuess
  
    GuessedLetters.append(guess)
    index = 0
  
    for letter in Word:
      if guess == letter:
        Answer[index] = guess
        CorrectGuess += 1
      index += 1
  
    alphabet.remove(guess)
    global IsPresent 
    IsPresent = False
    
    if CorrectGuess == len(Word):
      global Count
      CorrectGues = 0
      Count = 0
      win()

def win():
  final = "".join(Answer)
  print(f"Well done you survived. The word was {final}")
  input("Please enter any key to start again ")
  Answer.clear()
  WrongLetters.clear()
  GuessedLetters.clear()
  init()
  
def init():
  import os
  os.system('cls||clear')

  reset_alphabet()
  set_answer()
  
  global IsPresent
  global Count
  
  while Count != 0:
    print()
    print()
    print(f"Available Letters: {alphabet}")
    print(f"Wrong guesses: {WrongLetters}")
    print(f"Answer: {Answer}")
    guess = input("Enter a letter: ")
  
    check_if_letter_is_present(guess)
  
    while IsPresent == True:
      for letter in GuessedLetters:
        if guess == letter: 
          IsPresent = True
          guess = input("Please pick another letter: ")
        else: 
          IsPresent = False
          check_if_letter_is_present(guess)
          
    for letter in Word:
      if guess == letter:
        IsPresent = True
        break
      else:
        IsPresent = False
  
    if IsPresent == False:
      letter_is_wrong(guess)
    else:
      letter_is_correct(guess)

  print(f"You lose. The correct word was {Word}")
  input("Please enter any key to start again ")
  Answer.clear()
  WrongLetters.clear()
  GuessedLetters.clear()
  Count = 0
  init()
  
init()
