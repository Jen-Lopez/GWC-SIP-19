# import libraries
import json,re
from textblob import TextBlob
from PIL import Image
import matplotlib.pyplot as plot
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# search query
query = 'automation'

# open and read json file
file = open("tweets.json",'r')
all_tweets = json.load(file) # holds all data in file as a list
file.close()

# creat image mask
twitter_mask = np.array(Image.open('twitter.png').convert("RGBA"))

# concatenate all tweets into single string
entire_thing = ""
for line in all_tweets:
    result = re.sub(r"http\S+", "", line['text'])
    entire_thing += result

# create dictionary where "word": "frequency"
word_freq_dict = {}

# textblob object
tb_obj = TextBlob(entire_thing)

# common words
stopwords = set(STOPWORDS)
stopwords.update([query,'retweet','rt','https','thing','things','twitter','tweet','tweets','say','they','word','will','many','need','make'])

# filter mechanism
for word in tb_obj.words:
    if word.lower() in stopwords:
        continue
    if len (word) <= 3:
        continue
    if not word.isalpha():
        continue
    word_freq_dict[word.lower()] = tb_obj.word_counts[word.lower()]


# create cloud based on frequency
print ("...Generating WordCloud...\n")
wordcloud = WordCloud(
        background_color = "white",
        max_font_size = 100,
        max_words = 150,
        mask = twitter_mask
).generate_from_frequencies(word_freq_dict)

# create color from image
image_color = ImageColorGenerator(twitter_mask)

# interpolation makes image appear more smoothly
plot.figure(figsize=[7,7])
plot.imshow(wordcloud.recolor(color_func = image_color),interpolation = "bilinear")
plot.axis("off")
plot.show()
