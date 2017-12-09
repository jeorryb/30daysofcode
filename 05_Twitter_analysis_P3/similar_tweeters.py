import re
import sys
import string
import usertweets
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords




def similar_tweeters(user1, user2):
    u1tweets = usertweets.UserTweets(user1)
    u2tweets = usertweets.UserTweets(user2)
    u1text = [t.text for t in u1tweets]
    u2text = [t.text for t in u2tweets]
    u1tokens = [tokenize_tweets(t) for t in u1text]
    u2tokens = [tokenize_tweets(t) for t in u2text]
    u1filtered = remove_stop(u1tokens)
    u2filtered = remove_stop(u2tokens)
    return cos_sim(u1filtered, u2filtered)

def tokenize_tweets(tweet):
    lowers = tweet.lower()
    no_punc = lowers.translate(str.maketrans('','',string.punctuation))
    no_link = re.sub(r"http\S+", "", no_punc)
    tokens = word_tokenize(no_link)
    return tokens

def remove_stop(token_list):
    words_filtered = []
    wstop = set(stopwords.words('english'))
    for t in token_list:
        for x in t:
            if x not in wstop:
                words_filtered.append(x)
    return words_filtered

def cos_sim(words1, words2):
    wordcnt1 = Counter(words1)
    wordcnt2 = Counter(words2)
    words1 = list(wordcnt1.keys())
    words2 = list(wordcnt2.keys())
    wordvec1 = [wordcnt1.get(word1, 0) for word1 in words1]
    wordvec2 = [wordcnt2.get(word2, 0) for word2 in words2]
    len_1 = sum(wv1*wv1 for wv1 in wordvec1) ** 0.5
    len_2 = sum(wv2**wv2 for wv2 in wordvec2) ** 0.5
    dot = sum(wv1*wv2 for wv1,wv2 in zip(wordvec1, wordvec2))
    cosine = dot / (len_1 * len_2)
    return cosine




if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
