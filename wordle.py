"""
Defines the core functionality for the Wordle game.

The `word` variable holds the correct word for the Wordle game.

The `makeAGuess()` function takes a user's guess as a parameter and returns a hint string indicating how many letters in the guess are correct and in the right position ("G"), how many letters are in the word but in the wrong position ("Y"), and how many letters are not in the word ("-").

The `playwordle()` function runs the Wordle game, prompting the user for guesses and printing the hint for each guess. The game continues for 6 guesses, and the function returns `True` if the user guesses the word correctly, or `False` if the user runs out of guesses.
"""

# TASK A: Define a variable 'word' that holds the correct word for the wordle game
word = "magic"

# TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
def makeAGuess(guess):
  # TASK C:Define a variable 'hint' that holds an empty string
  hint = ""

  # TASK D: Build a loop that loops from 0 to the length of word
  for i in range(len(word)):
    
    # TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
    if guess[i] == word[i]: 
      hint += "G"
    
    # TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
    elif guess[i] in word:
      hint += "Y"

    # TASK G: If the previous two conditions are false, add the symbol "-" to the hint
    else: 
      hint += "-"
    
  # TASK H: Return hint
  return hint
  

def playwordle():
  print("Let us play wordle! Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. G represents a letter in the word and in the correct spot.. Y represents a letter in the word but in the wrong spot. - represents a letter not in the word in any spot. State your guess.")

  # TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
  for i in range(6):
    # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable
    guess = input("make your guess: ")
    # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable
    hint = makeAGuess(guess)
    # TASK L: Print hint
    print(hint)
    # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
    if hint == "GGGGG":
      print("you won!")
      return True

  # TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 
  if hint != "GGGGG":
    print("'It seems like you're not ready yet. Come back another time... maybe you'll find something that can help you..'")
    print("you decide to head back to the field")
    return False
