from random import randint


class Board:
    def __init__(self, level):

        self.voltorbs = set()

        self.row_voltorbs = [0, 0, 0, 0, 0]
        self.col_voltorbs = [0, 0, 0, 0, 0]

        self.game_board = [[]]

        self.calculate_row_voltorbs(level)
        self.fill_board()

    def calculate_row_voltorbs(self, level):
        num_voltorbs = 6
        row = 0
        while num_voltorbs > 0:
            amount = randint(0, num_voltorbs - level + 1)

            if self.row_voltorbs[row] + amount <= 5:
                num_voltorbs -= amount
                self.row_voltorbs[row] += amount

            if row == 4:
                row = 0
            else:
                row += 1

    def fill_board(self):
        for row in range(len(self.row_voltorbs)):
            cols = list(range(0, 5))

            for amount in range(self.row_voltorbs[row]):
                i = randint(0, len(cols) - 1)
                col = cols.pop(i)

                if self.col_voltorbs[col] < 5:
                    self.col_voltorbs[col] += 1
                    self.voltorbs.add((row, col))
                else:
                    col = cols.pop(randint(0, len(cols) + 1))
                    self.col_voltorbs[col] += 1
                    self.voltorbs.add((row, col))

    def get_col_voltorbs(self):
        return self.col_voltorbs

    def get_row_voltorbs(self):
        return self.row_voltorbs

    def check_voltorb(self, voltorb):
        return voltorb in self.voltorbs


b = Board(1)





