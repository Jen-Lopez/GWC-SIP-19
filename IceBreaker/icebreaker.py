#import modules
import csv
import random

#read file
with open ("Icebreak.csv", "r") as ice:
    reader = csv.reader(ice)
    data = [row for row in reader]

called  = list() # This list has questions already called

#generate random Q NUMBER
def gen():
    num = random.randint(0,len(data)-1)
    return num

#generate random QUESTION; repeats until new question not answered is generated
def res():
    while (True):
        qnum = gen()
        if (qnum not in called):
            print ("%d. %s" %(qnum+1, data[qnum][0]))
            called.append(qnum) #add question to called list
            break

# ---------------------- MAIN PROGRAM ----------------------
iter = 0
ice_len = len(data)

while (True):
    try: #exception raised if input is not number
        studs = int(input ("\nHow many students are there? "))
        if not studs > 0:
            print ("There can't be no students!") # can only be positive
            continue
        break
    except Exception as e:
        print ("Not a number! Try again.")

while (True):
    iter += 1

    if iter > ice_len: # runs if there are more students than questions; resetting necessary
        print("\nThere are no more icebreaker questions.")
        while True:

            rep = input ("\nWant to repeat? (y/n) ")
            if (rep.isalpha() and (rep == "y" or rep == "n")):
                rep.lower()
                break
            else:
                print ("Try Again.\n")
                continue
        if rep == "y":
            print ("\nresetting...")
            del called[:]
            iter = 0
            continue
        elif rep == "n":
            print("\nquitting...\n")
            break

    if iter > studs: # asks if you want to continue once you reach x q's for x students
        while True:
            ans = input ("\nMore questions? (y/n) ")
            if ans.isalpha() and (ans == "y" or ans == "n"):
                ans = ans.lower()
                break
            else:
                print ("Try Again.")
                continue
        if ans == "y":
            iter = 0
            print ("\ngenerating...")
        elif ans == "n":
            print("\nquitting...\n")
            break

    uin = input()
    if (uin == ""): #if you press enter, empty string
        res() #function called to generate/print question

    elif (uin == "q"):
        print("\nquitting...\n")
        break
    else:
        iter -= 1
        print ("unknown key\n")
