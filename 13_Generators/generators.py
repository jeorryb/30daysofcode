import os
import fnmatch
import re
from operator import itemgetter

"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

def gen_files(pat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, pat):
            yield os.path.join(path,name)

def gen_lines(files):
    for file in files:
        with open(file) as f:
            for line in f:
                yield line

def gen_grep(lines, pattern):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield pat.search(line).group(2)


def gen_count(wordgrep):
    words = {}
    for word in wordgrep:
        words[word] = words.get(word, 0) + 1
    return words


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('*.py', '/Users/jeorryb/Dropbox/30daychallenge/challenges/')
    lines = gen_lines(files)
    greps = gen_grep(lines, '(^import) (\w*)')
    words = gen_count(greps)
    sorted_words = sorted(words, key=lambda x: words[x], reverse=True)
    for k in sorted_words:
        print(f'{words[k]} {k}')

