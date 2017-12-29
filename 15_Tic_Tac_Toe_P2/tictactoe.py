import random

DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)


class TicTacToe:

    def __init__(self):
        '''Constructor, below worked well for us ...'''
        self.board = [None] + VALID_POSITIONS  # skip index 0
        self.board = [str(x) for x in self.board]

    def __str__(self):
        '''Print the board'''
        self.layout = ('\n' * 80 +
                       '   |   |\n' +
                       ' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + '\n' +
                       '-----------\n' +
                       '   |   |\n' +
                       ' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + '\n' +
                       '-----------\n' +
                       '   |   |\n' +
                       ' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3] + '\n' +
                       '   |   |')
        return self.layout

    def inputplayerletter(self):
        self.letter = ''
        while not (self.letter == "O" or self.letter == "X"):
            print('Do you want to be X or O?')
            self.letter = input().upper()
        if self.letter == 'X':
            self.letters = ['X', 'O']
        else:
            self.letters = ['O', 'X']
        return self.letters

    def firstplayer(self):
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def playagain(self):
        print('Do you want to play again? (y or n)')
        return input().lower().startswith('y')

    def makemove(self, board, letter, move):
        board[move] = letter

    def iswinner(self, board, letter):
        for a, b, c in WINNING_COMBINATIONS:
            if board[a] == letter and board[b] == letter and board[c] == letter:
                return True
        return False

    def isspacefree(self, board, move):
        if (board[int(move)] == 'X') or (board[int(move)] == 'O'):
            return False
        else:
            return True

    def getplayermove(self, board):
        move = ' '
        while move not in list('123456789') or not self.isspacefree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooserandmove(self, board, moves):
        possmoves = []
        for x in moves:
            if self.isspacefree(board, x):
                possmoves.append(x)
        if len(possmoves) != 0:
            return random.choice(possmoves)
        else:
            return None

    def getcopy(self, board):
        dupeboard = []
        for i in board:
            dupeboard.append(i)
        return dupeboard

    def getcompmove(self, board, completter):
        if completter == 'X':
            playerletter = 'O'
        else:
            playerletter = 'X'

        for i in range(1, 10):
            copy = self.getcopy(board)
            if self.isspacefree(copy, i):
                self.makemove(copy, completter, i)
                if self.iswinner(copy, completter):
                    return i

        for i in range(1, 10):
            copy = self.getcopy(board)
            if self.isspacefree(copy, i):
                self.makemove(copy, playerletter, i)
                if self.iswinner(copy, playerletter):
                    return i

        move = self.chooserandmove(board, [1, 3, 7, 9])
        if move is not None:
            return move

        if self.isspacefree(board, 5):
            return 5

        return self.chooserandmove(board, [2, 4, 6, 8])

    def boardfull(self, board):
        for i in range(1, 10):
            if self.isspacefree(board, i):
                return False
        return True










    # TODOS:
    # Complete: display board in __str__ (clearing screen)
    # Complete: ask user for X or O
    # have at least an is_win method to exit game
    # num turns = len(VALID_POSITIONS) so might not need is_draw (tie) method
    # have method(s) to get user input and validate
    # if playing against computer (AI) calculate next best move (algorithm)
    # update board upon each turn


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    while True:
        game = TicTacToe()
        playerletter, completter = game.inputplayerletter()
        turn = game.firstplayer()
        print('The' + turn + ' will go first.')
        gameisplaying = True

        while gameisplaying:
            if turn == 'player':
                print(game)
                move = game.getplayermove(game.board)
                game.makemove(game.board, playerletter, move)

                if game.iswinner(game.board, playerletter):
                    print(game)
                    print('Hooray! You have won the game!')
                    gameisplaying = False
                else:
                    if game.boardfull(game.board):
                        print(game)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = game.getcompmove(game.board, completter)
                game.makemove(game.board, completter, move)

                if game.iswinner(game.board, completter):
                    print(game)
                    print('The machines have won! You lose.')
                    gameisplaying = False
                else:
                    if game.boardfull(game.board):
                        print(game)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
        if not game.playagain():
            break
        # take turn
        # make move
        # check win - break
        #
        # ask if another game, if n - break
