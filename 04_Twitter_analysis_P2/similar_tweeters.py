import re
import sys
import string
import usertweets
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords




def similar_tweeters(user1, user2):
    u1tweets = usertweets.UserTweets(user1)
    u2tweets = usertweets.UserTweets(user2)
    u1text = [t.text for t in u1tweets]
    u2text = [t.text for t in u2tweets]
    u1tokens = [tokenize_tweets(t) for t in u1text]
    u2tokens = [tokenize_tweets(t) for t in u2text]

def tokenize_tweets(tweet):
    lowers = tweet.lower()
    no_punc = lowers.translate(str.maketrans('','',string.punctuation))
    no_link = re.sub(r"http\S+", "", no_punc)
    tokens = word_tokenize(no_link)
    return tokens

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
