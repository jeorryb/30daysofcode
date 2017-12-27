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


    def draw_board(self):
        '\n' * 80
        '   |   |\n'
        ' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + '\n'
        '-----------\n'
        '   |   |\n'
        ' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + '\n'
        '-----------\n'
        '   |   |\n'
        ' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3]  + '\n'
        '   |   |'



    def __str__(self):
        '''Print the board'''
        layout = ('\n' * 80 +
                 '   |   |\n' +
                 ' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + '\n' +
                 '-----------\n' +
                 '   |   |\n' +
                 ' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + '\n' +
                 '-----------\n' +
                 '   |   |\n' +
                 ' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3]  + '\n' +
                 '   |   |')
        return layout
        



    # TODOS:
    # display board in __str__ (clearing screen)
    # have at least an is_win method to exit game
    # num turns = len(VALID_POSITIONS) so might not need is_draw (tie) method
    # have method(s) to get user input and validate
    # if playing against computer (AI) calculate next best move (algorithm)
    # update board upon each turn


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        # take turn
        # make move
        # check win - break
        #
        # ask if another game, if n - break
