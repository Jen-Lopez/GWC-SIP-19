import json

# load tweets file, which holds twitter data
twitter_file = open("tweets.json",'r')
tweet_data = json.load(twitter_file)
twitter_file.close() # close the file after reading

for t in range (len(tweet_data)): #iterate through json data
    user_name = tweet_data[t]["user"]["name"].upper() # extract the twitter user
    tweet = tweet_data[t]['text'] # extract the tweet

# if the location is available, print it.
# Otherwise, only print the twitter user's name and tweet

    try:
        location = tweet_data[t]["user"]["location"]
        print ("Twitter user %s from %s says: \n%s\n" %(user_name,location,tweet))
    except:
        print ("Twitter user %s says: \n%s\n" %(user_name,tweet))
        continue
