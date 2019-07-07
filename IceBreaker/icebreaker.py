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
count = 0  #records num of q's answered

while (True):
    try: #exception raised if input is not number
        studs = int(input ("\nHow many students are there? "))
        break
    except Exception as e:
        print ("Not a number! Try again.")

while (True):
    uin = input()
    if (uin == ""): #if you press enter, empty string
        res() #function called to generate/print question
        count +=1 #keeps track of how many q's were answered
    elif (uin == "q"):
        print("\nquitting...")
        break
    else:
        print ("unknown key")


#things needed to do:
    # Include students by either stopping until students = count or resetting list if there are more students than q's
