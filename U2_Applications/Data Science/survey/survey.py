import json

survey = ["What is your name?","Where do you live?","Do you have a pet? If so, what kind?","What is your favorite movie?","Favorite place to go to?","Most Frequently Used App?"]
keys = ["name","home", "pets","movie","place", "app"]
all_answers = []

print ("\nPress 'Enter' to begin the survey or 'q' to quit.")

while True:
    print()
    responses = {}
    res = input()

    if (res == ""):
        for i in range(len(survey)):
            res = input(survey[i] + " ")
            responses[keys[i]] = res
        all_answers.append(responses)
    elif ( res == "q"):
        print("...quitting...\n")
        break
    else:
        print("Invalid input. 'Enter' to continue or 'q' to quit.")

file = open("response_data.json",'r')
data = json.load(file)
all_answers.extend(data)
file.close()

file = open("response_data.json",'w')
file.write('[\n')

for i in range (len(all_answers)):
    if (i < len(all_answers)-1):
        json.dump(all_answers[i],file)
        file.write(',\n')
    else:
        json.dump(all_answers[i],file)
        file.write('\n')

file.write(']')
file.close()

def num_responses():
    return len(all_answers)

print("~~ Statistics ~~")
print ("Number of responses: %d\n" %(num_responses()))
