# implements starter code
import random

potential_words = ["brownie", "sandwich", "nuggets", "fries", "hot dog", "cake"]

word = random.choice(potential_words) #chooses random word from the list

# Converts the word to lowercase
word = word.lower() # avoids case sensitivity

# Make it a list of letters for someone to guess
current_word = ["_",]*len(word)

# Some useful variables
guesses = []
maxfails = 7
fails = 0
won = False # keeps track of whether user won or not

while fails < maxfails: # this code runs until we reach 7 maxfails
    print ("GUESSES: ", guesses)
    guess = input("Guess a letter ('1' to solve): ") # holds user input
    if (guess == "1"): # This key allows user to enter their word guess
        res = (input ("Do you want to solve? (y/n) ")).lower() # user allowed to enter whole word if they know
        if (res == "y"):
            ans = (input("What's the word? ")).lower()
            if ans == word: # if the user got the word right, end game
                won = True
                break
            else:
                print ("Incorrect word!\n")
                fails += 1 # increases failed attempts
                continue
        else: # if res is "n" or anything else, return to beginning
            print()
            continue

    try:
        guess = guess.lower()
        if len(guess) > 1 or (guess in guesses):
            raise Exception('Invalid Guess!')
    except Exception as e:
        print("Invalid Input!\n")
        continue

	# avoids non-letters, more than one letter, duplicate letters

    guesses.append(guess) # adds user input to list of guesses in order to avoid duplicates
    for i in range (len(word)):
        if (word[i] == guess): # updates the underscores to correct letters
            current_word[i] = guess

    if ("_" not in current_word): # if user inputted all letters correctly, win game
        won = True
        break

    print(current_word)
    fails += 1 # you only fail if the input is not in the word.
    if (fails != maxfails):
        print("You have " + str(maxfails - fails) + " tries left!\n")

if not won:
    print ("\nYou Lost! The word was %s. Thanks for playing!\n" %(word.upper()))
else:
    print("\nYou won! Thanks for playing!\n")
