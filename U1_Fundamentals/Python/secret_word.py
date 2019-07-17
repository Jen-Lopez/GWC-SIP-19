#create a list of words
#randomly generate a word to be guessed
# print blank underscores to represent unsolved word
# create a list of letters that have been said already
# update the word as letters are said
# track the amount of mistakes the player makes

import random
food_list = ["apple", "banana", "chocolate cake", "pizza","quiche", "taco", "cereal","donuts","cherries", "nuggets"]

word = random.choice(food_list)

intro = """
Hello! Welcome to Guess The Secret Word.
You will have 8 tries to guess the word. The topic is food.
Goodluck!
"""
secret_word = "_" * len(word)
said_letters = list()
guesses = 0

print (intro)
print ("This is your secret word:", secret_word, "WORD LENGTH:",len(secret_word))

while guesses < 8:
    guesses +=1
    index = 0
    indexes = list()
    solved = False

    print ("\nTry #",guesses)
    print ("Letters Used: ", said_letters)
    print ("Word:",secret_word)
    user_letter = input ("Enter a letter (or '1' to solve): ")
    if not(user_letter.isalpha() or user_letter == "1"):
        print ("\nInvalid input. Only letters or '1' to solve!")
        continue

    if user_letter == "1":
        res = input ("\nDo you want to solve? (y/n) ")
        if res == "y":
            guess = input ("\nWhat's the word? ")
            if guess == word:
                print ("\nCongratulations. You Won!\n")
                solved = True
                break
            else:
                print ("Incorrect.\n")
                continue
        elif res == "n":
            guesses -= 1 # won't count towards you
            continue
        else:
            print ("Unacceptable input.\n")
            continue

    if user_letter not in said_letters:
        said_letters.append(user_letter)
    else:
        print ("\nThis letter has already been said!\n")
        continue

    if user_letter in word:
        for c in word:
            if c == user_letter:
                indexes.append(index)
            index += 1
        for i in indexes:
            secret_word = secret_word[:i] + user_letter + secret_word[i+1:]
        print ("\nNew Word:",secret_word, "\n")
    else:
        print ("\nIncorrect Try Again!")

    if secret_word == word:
        solved = True
        print ("Congratulations! You solved it!")
        break

if not solved:
    print ("\nUnfortunately, the secret word was:", word)

print ("Thanks for playing!\n")
