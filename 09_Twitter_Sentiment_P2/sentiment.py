import json
import re
import sys
from textblob import TextBlob

IS_LINK_OBJ = re.compile(r'^(?:@([A-Za-z0-9_]+)|https?://)')
IS_RT = re.compile(r'^RT')


def read_json(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)

def _is_ascii(w):
    return all(ord(c) < 128 for c in w)


def clean_text(tweet):
    tweet = tweet.split()
    tweet = [word for word in tweet if _is_ascii(word)]
    tweet = [word for word in tweet if not IS_LINK_OBJ.search(word)]
    tweet = [word for word in tweet if not IS_RT.search(word)]
    tweet = ' '.join(tweet)
    return tweet



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please provide json data file')
        sys.exit(1)
    input_file = sys.argv[1]
    tweets = read_json(input_file)
    sentiments = []
    for tw in tweets:
        tweet = dict(tw)['text']
        tweet = clean_text(tweet)
        tb = TextBlob(tweet)
        sentiments.append(tb.sentiment.polarity)
    average = sum(sentiments) / len(sentiments)
    print(f'The average sentiment is {average}')
