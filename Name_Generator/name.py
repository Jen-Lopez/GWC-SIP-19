#import modules
import csv
import random

#read file
with open ("roster.csv", "r") as ros:
    reader = csv.reader(ros)
    data = [row for row in reader]

called  = list() # This list has questions already called

#generate random Q NUMBER
def gen():
    num = random.randint(0,len(data)-1)
    return num

#generate random QUESTION; repeats until new name is generated
def call():
    while (True):
        qnum = gen()
        if (qnum not in called):
            print (data[qnum][0])
            called.append(qnum) #adds name to called list
            break

# ---------------------- MAIN PROGRAM ----------------------
print ("Press 'Enter' to generate names")
stud = len(data)
iter = 0
# stop at a certain point until the last student is reached and reset the list
while (True):
    iter += 1
    if (iter > stud):
        print  ("\nEveryone was called!")
        while (True):
            res = input ("\nReset the generator? (y/n) ")

            if res.isalpha():
                res = res.lower()
                if res == "y" or res == "n":
                    break
            else:
                print ("Try Again.")
                continue

        if res == "y": # if yes, reset.
            print ("\nresetting list....") #reset the list
            del called[:] # reset called list
            iter = 0 # reset current iteration
            print("\nPress 'Enter' to start generating")
            continue # continue while loop until we enter 'q' or repeat again
        elif res == "n": # if no, quit.
            print ("\nquitting...")
            break

    uin = input()
    if (uin == ""): #if you press enter, empty string
        call () #function called to generate/print name

    elif (uin == "q"):
        print("\nquitting...\n")
        break
    else:
        print ("unknown key\n")
