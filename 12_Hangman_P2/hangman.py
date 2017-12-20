from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
# ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.turn = hang_graphics()
        self.allowed = len(list(hang_graphics()))
        self.word = word
        self.letters = [x for x in self.word.lower()]
        self.blanks = ['_'] * len(self.word)
    
    def bad_guess(self):
        print('Sorry, you have chosen poorly')
        print(next(self.turn))
        self.allowed -= 1

    def good_guess(self, letter):
        self.letter = letter
        pos = [i for i, j in enumerate(self.letters) if j == self.letter]
        for x in pos:
            self.blanks[x] = self.letter
        return self.blanks

    def you_win(self):
        congrats = print('Congratulations! You Win')
        return congrats




if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()

    game = Hangman(word)

    while True:
        print(game.blanks)
        guess = input('Make a guess: ')
        if guess.lower() == word.lower():
            game.you_win()
            break
        elif guess in game.letters:
            game.blanks = game.good_guess(guess)
        else:
            if game.allowed == 1:
                print('Sorry, You lost')
                print(next(game.turn))
                break
            else:
                game.bad_guess()
