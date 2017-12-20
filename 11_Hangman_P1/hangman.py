from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.turn = hang_graphics()
        self.word = word
        self.letters = [x for x in self.word.lower()]
        self.blanks = ['_'] * len(self.word)
    
    def bad_guess(self):
        print('Sorry, you have chosen poorly')
        print(next(self.turn))
        ALLOWED_GUESSES -= 1

    def good_guess(self, letter):
        self.letter = letter
        pos = [i for i, j in enumerate(self.letters) if j == self.letter]
        for x in pos:
            self.blanks[x] = self.letter
        return self.blanks




if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()

    game = Hangman(word)
    print(game.blanks)
    guess = input('Make a guess: ')
