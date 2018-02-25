# Create dictionaries that translate Alexa-user conversation hit words to poems
# Qian Yang (yang-qian@github, yangqian@cmu.edu)

#import os.path, time
#print("===\nCreated by: Qian Yang")
#print("last modified: %s" % time.ctime(os.path.getmtime(os.path.abspath(__file__))),'\n===')

### Related work: 
# Poetry sentiment analysis: https://masta-g3.github.io/linear-content/sentiment-bukowski.html

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# https://divinationandfortunetelling.com/articles/2017/8/28/planet-correspondences-in-astrology-tarot-and-divination
semantic_dict = {'The Sun':
                {'symbol': ['laurel wreath', 'lyre'],
                 'sentiment': 'pos',
                 'keyword': ['life', 'conscious', 'identity', 'success', 'positivity', 'fame', 'victory']
                },
                'The Moon':
                {'symbol': ['Crab', 'Water', 'Ocean', 'Female'],
                 'sentiment': 'n/a',
                 'keyword': ['females', 'subconscious', 'secrets', 'infidelity', 'emotions', 'reputation', 'dreaming', 'creativity']
                },
                'Venus':
                {'symbol': ['Shell', 'Myrtle', 'Rose', 'Swan', 'Girdle'],
                 'sentiment': 'pos',
                 'keyword': ['Love', 'Desire', 'Relationships', 'Beauty', 'Harmony', 'Fertility']
                },
                'Mars':
                {'symbol': ['Swords', 'Shield', 'Spear', 'Helmet', 'Boar'],
                 'sentiment': 'pos',
                 'keyword': ['Aggression', 'Will', 'Anger', 'Drive', 'Determination', 'War']
                },
                'Saturn':
                {'symbol': [],
                 'keyword': ['Luck', 'Fortune', 'Expansion', 'Leadership', 'Charity', 'Confidence']
                    
                },
                'Uranus':
                {'symbol': ['The sky'],
                 'keyword': ['Originality', 'Technology', 'Change', 'Individuality']
                }
                
               }


def weather_to_poem(w_kw):
    """
    if the keyword is in semantic_dict, return a poem/tweet that contains the symbol,
    on the same topic, and (if possible) also fits the sentiment;
    if the keyword is NOT in semantic_dict, return a neutral poem/tweet.
    PARA:: w_kw, weather keyword (str). i.e. sunny, warm, snowy, windy, cozy
    OUTPUT:: alexa (str)
    """
    pass

def poem_sentiment(poem):
    """
    Determine the sentiment of a sentence using a Microsoft pre-trained model
    (https://docs.microsoft.com/en-us/machine-learning-server/python-reference/microsoftml/get-sentiment)
    
    para:: a poem (string);
    output:: sentiment score (1 = positive, 0 = negative)
    """
    analyzer = SentimentIntensityAnalyzer()

    sentence = poem.split('\n')[0]
    vs = analyzer.polarity_scores(sentence) # sentiment score as dict
#    print(sentence, vs['neu'], vs['neg'], vs['compound'], vs['pos'])
    # print("{:-<65} {}".format(sentence, str(vs)))
    return (vs['pos'], vs['neg'], vs['neu'], vs['compound'])



    

    

