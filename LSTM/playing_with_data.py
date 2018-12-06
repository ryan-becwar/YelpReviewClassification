import numpy as np
import pandas as pd

df = pd.read_csv('10000_reviews.csv')
df.drop(columns=['Unnamed: 0'],inplace=True)

text = list(df['text'])

numWords = []

for line in text:
    count = len(line.split())
    numWords.append(count)

import matplotlib.pyplot as plt

plt.hist(numWords)
plt.show()

maxSeqLength = 250

# Removes punctuation, parentheses, question marks, etc., and leaves only alphanumeric characters
import re
strip_special_chars = re.compile("[^A-Za-z0-9 ]+")

def cleanSentences(string):
    string = string.lower().replace("<br />", " ")
    return re.sub(strip_special_chars, "", string.lower())

