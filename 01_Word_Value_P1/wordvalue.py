from data import DICTIONARY, LETTER_SCORES

def load_words(dictfile=DICTIONARY):
    """Load dictionary into a list and return list"""
    try:
        with open(dictfile) as f:
            websters = f.readlines()
            websters = [x.strip() for x in websters]
            return websters
    except TypeError:
        return dictfile

def calc_word_value(word, score=0):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    for w in word:
        if not w.isalpha():
            continue
        score += LETTER_SCORES[w.upper()]
    return score

def max_word_value(wordlist=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    wordscores = []

    websters = load_words(dictfile=wordlist)
    for word in websters:
        score = calc_word_value(word)
        entry = (word, score)
        wordscores.append(entry)
    wordscores = sorted(wordscores, key=lambda x: x[1], reverse=True)
    return wordscores[0][0]
    
    

if __name__ == "__main__":
    pass # run unittests to validate
