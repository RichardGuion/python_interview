import random

'''
https://gist.github.com/josephdwyer/7f7c61054b86553133cfce5a01abe10c

We are too lazy and/or cheap to purchase a real copy of the game Connect Four, so we have decided to make our own.
Game

Connect Four is a two-player game in which the players take turns dropping colored discs from the top into a seven-column, six-row vertically-suspended grid. The pieces fall straight down, occupying the next available space within the column. A player wins when 4 pieces of their color are in a row in any direction.

Task:

Implement a MakeMove function that will be called when a player selects a column
Next, add the ability to detect when a player has won
'''


class connect4:
    def __init__(self, height = 6, width = 7):
        self._matrix = [[' ' for x in range(width)] for y in range(height)]
        self._pieces = ['x', 'o']
        self._height = height
        self._width = width


    def print_game_board(self):
        for row in self._matrix:
            print(row)


    def get_rand_col(self):
        return random.randint(0, len(self._matrix[0])-1)


    def get_rand_piece(self):
        return self._pieces[random.randint(0, 1)]


    def is_matrix_filled(self):
        filled_count =0
        for col in range(self._width):
            if self._matrix[0][col] != ' ':
                filled_count += 1
        return filled_count == self._width


    def make_move(self, char):
        col = self.get_rand_col()
        for row in reversed(range(len(self._matrix))):
            if self._matrix[row][col] == ' ':
                self._matrix[row][col] = char
                return self.check(row, col)
        if not self.is_matrix_filled():
            print(f'retrying this move, all column slots filled for {col}')
            self.print_game_board()
            return self.make_move(char)
        else:
            # the game can no longer continue
            return None, None


    def eval_symbol(self, col, consecutive_count, index, prev_symbol):
        if prev_symbol != ' ' and self._matrix[index][col] == prev_symbol:
            consecutive_count += 1
        else:
            consecutive_count = 0
            prev_symbol = self._matrix[index][col]
        return consecutive_count, prev_symbol


    def check(self, row, col):
        if self._height - row >= 3:
            consecutive_count = 0
            prev_symbol = self._matrix[row][col]
            for index in range(row, self._height):
                consecutive_count, prev_symbol = self.eval_symbol(col, consecutive_count, index, prev_symbol)
                if consecutive_count > 3:
                    print(f'Col {col} filled')
                    return row, col

        if col >= 3:
            consecutive_count = 0
            prev_symbol = self._matrix[row][col]
            for index in range(col, 0, -1):
                consecutive_count, prev_symbol = self.eval_symbol(index, consecutive_count, row, prev_symbol)
                if consecutive_count > 3:
                    print(f'Row {row} filled to the left')
                    return row, col

        if self._width - col >= 3:
            consecutive_count = 0
            prev_symbol = self._matrix[row][col]
            for index in range(col, self._width):
                consecutive_count, prev_symbol = self.eval_symbol(index, consecutive_count, row, prev_symbol)
                if consecutive_count > 3:
                    print(f'Row {row} filled to the right')
                    return row, col

        # TODO: diagonal check left
        # TODO: diagonal check right

        return -1, -1



con = connect4()
for move in range(100):
    pt = con.make_move(con.get_rand_piece())
    if pt == (None, None):
        print("NO WINNER AT ALL...")
        break
    elif pt != (-1, -1):
        print(f'A WINNER!!! at {pt}')
        break
con.print_game_board()
