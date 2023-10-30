# Import the 'random' module to generate random numbers
import random

# Welcome message
print("Welcome to hangman")
print("-------------------------------------------")

# Define a list of words for the hangman game
wordDictionary = ["sunflower", "house", "diamond", "memes", "yeet", "hello", "howdy", "like", "subscribe"]

# Choose a random word from the word list
randomWord = random.choice(wordDictionary)

# Print underscores for each letter in the random word to represent the unguessed letters
for x in randomWord:
  print("_", end=" ")

# Function to print the hangman based on the number of wrong guesses
def print_hangman(wrong):
  if wrong == 0:
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif wrong == 1:
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  # Continue this pattern for each stage of the hangman drawing

# Function to print the guessed letters and underscores for unguessed letters
def printWord(guessedLetters):
  counter = 0
  rightLetters = 0
  for char in randomWord:
    if char in guessedLetters:
      print(randomWord[counter], end=" ")
      rightLetters += 1
    else:
      print(" ", end=" ")
    counter += 1
  return rightLetters

# Function to print lines to separate the word display
def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

# Calculate the length of the word to guess
length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

# Main game loop
while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
  # Display letters guessed so far
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")

  # Prompt the user to input a letter guess
  letterGuessed = input("\nGuess a letter: ")

  # Check if the guessed letter is correct
  if randomWord[current_guess_index] == letterGuessed:
    # Print hangman
    print_hangman(amount_of_times_wrong)
    current_guess_index += 1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  else:
    amount_of_times_wrong += 1
    current_letters_guessed.append(letterGuessed)
    # Update the drawing
    print_hangman(amount_of_times_wrong)
    # Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()

# Game over message
print("Game is over! Thank you for playing :)")
