#imports the ability to get a random number (we will learn more about this later!)
from random import *
# * is a wild card!

#Generates a random integer between 1-20 (INCLUSIVE).
aRandomNumber = randint(1, 20)

# ---------- WHILE LOOP ----------
tries = 0
while tries < 3:
	guess = input ("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric():
		print ("That's not a positive whole number, try again!\n")
		continue
	else:
		guess = int(guess)
		tries +=1
		if (not(guess <=20) or not(guess >= 1)):
			print ("Your guess is not between 1 and 20! \n")
			continue

	if (guess == aRandomNumber): # We got the number!
		print ("You got it after ... ", end = '') # this would make the next print statement print on the same line
		if (tries == 1):
			print ("1 try")
		else:
			print (tries, "tries")
		break # exit out of loop and "jump" to the following if statement
	elif (guess  < aRandomNumber): # tell user to aim higher if the guess is low
		if (tries !=3):
			print ("You're too Low. Aim Higher!\n")
	else:
		if (tries != 3):
			print ("You're too High. Aim Lower!\n") # tell user to aim lower if the guess is too high

if (guess!= aRandomNumber): # if the user did not guess correctly, then we display the number.
	print ("\nThe number was:", aRandomNumber)

print ("\nThanks for playing!") # The End

# ---------- FOR LOOP ----------
# for i in range (3): #repeats three times
# 	#guess stores the user input value
# 	guess = input("Guess a number between 1 and 20 (inclusive): ")
# 	if not guess.isnumeric(): # checks if a string is only digits 0 to 9/is an integer
# 		print("That's not a positive whole number, try again!\n")
# 		continue # goes back to the beginning
# 	else:
# 		guess = int(guess) # converts a string to an integer; guess is "updated" to an integer form
# 		if (not (guess <= 20) or not(guess >=1)): #verifies if the integer is between 1 and 20
# 			print ("Your guess is not between 1 and 20!\n")
# 			continue #goes back to the beginning
#
# 	if (guess == aRandomNumber): # We got the number!
# 		print ("You got it!\n")
# 		break # exit out of loop and "jump" to the following if statement
# 	elif (guess  < aRandomNumber): # tell user to aim higher if the guess is low
# 		print ("You're too Low. Aim Higher!\n")
# 	else:
# 		print ("You're too High. Aim Lower!\n") # tell user to aim lower if the guess is too high
#
# if (guess!= aRandomNumber): # if the user did not guess correctly, then we display the number.
# 	print ("The number was:", aRandomNumber)

#print ("Thanks for playing!") # The end
