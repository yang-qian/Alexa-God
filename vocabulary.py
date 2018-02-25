# Create a set of vocabularies
# Qian Yang (yang-qian@github, yangqian@cmu.edu)
## OUTPUT: poems.json
## Schema: text, topic, sentimen (pos,neg,compo)


#import os.path, time
#print("===\nCreated by: Qian Yang")
#print("last modified: %s" % time.ctime(os.path.getmtime(os.path.abspath(__file__))),'\n===')

from semantics import *
import csv,json
import pandas as pd


# ======== POEMS from poetryfuncation.org ======== #

poems_dict = {}

with open('poems-from-poetryfoundation-org.csv', 'r', encoding = 'utf-8') as fin:
    reader = csv.reader(fin)
    # print(next(reader)) # ignore old header

    for row in reader:
        author, content, name,  age, _type = row
        
        # break down content into sentences
        for line in content.split('.'):
            line += '.'
            pos, neg, neu, compound = poem_sentiment(line)
            poems_dict[line.lstrip()] = {'poem name': name ,
                                'type': _type,
                                'pos': pos,
                                'neg': neg,
                                'neu': neu,
                                'compound': compound}

print(poems_dict)
# write into json file
with open('poems.json', 'w') as fp:
    json.dump(poems_dict, fp)

astro = pd.read_csv("poetastrologers_cleaned_tweets.csv",
                   header = None,
                   names = ['content'])

#poem_sentiment(poems)
