from random import randint

# Game Info Source: https://bulbapedia.bulbagarden.net/wiki/Voltorb_Flip#Gameplay


# There are 5 potential level boards per level.
def get_level_board(level):
    if level == 1:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]
    # TODO Put in correct values for all the levels above 1
    elif level == 2:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]
    elif level == 3:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]
    elif level == 4:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]
    elif level == 5:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]
    elif level == 6:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]
    elif level == 7:
        level_1 = [(3, 1, 6), (0, 3, 6), (5, 0, 6), (2, 2, 6), (4, 1, 6)]
        return level_1[randint(0, 4)]


class Board:
    def __init__(self, level):

        self.level_board = get_level_board(level)

        self.spaces = {}

        self.row_voltorbs = [0, 0, 0, 0, 0]
        self.col_voltorbs = [0, 0, 0, 0, 0]

        self.row_points = []
        self.col_points = []

        self.calculate_row_voltorbs()
        self.fill_board()
        self.get_points()

    # determines how many voltorbs are in each row
    def calculate_row_voltorbs(self):
        num_voltorbs = self.level_board[2]
        row = 0
        while num_voltorbs > 0:
            if num_voltorbs > 5:
                amount = randint(0, 5)
            else:
                amount = randint(0, num_voltorbs)

            if self.row_voltorbs[row] + amount <= 5:
                num_voltorbs -= amount
                self.row_voltorbs[row] += amount

            if row == 4:
                row = 0
            else:
                row += 1

    # Determines which columns to place Voltorbs in and stores the index
    def fill_board(self):
        for row in range(len(self.row_voltorbs)):
            cols = list(range(0, 5))

            for amount in range(self.row_voltorbs[row]):
                i = randint(0, len(cols) - 1)
                col = cols.pop(i)

                while self.col_voltorbs[col] > 5:
                    col = cols.pop(randint(0, len(cols) + 1))

                self.col_voltorbs[col] += 1
                self.spaces[(row, col)] = 0

    # Determines which spaces will hold x2s and x3s multipliers
    def get_points(self):
        for vol in self.row_voltorbs:
            self.row_points.append(5 - vol)

        for vol in self.col_voltorbs:
            self.col_points.append(5 - vol)

        # Place x2 multipliers on board
        for point in range(0, self.level_board[0]):

            rand_ind = (randint(0, 4), randint(0, 4))

            while rand_ind in self.spaces.keys() or self.row_voltorbs[rand_ind[0]] == 5 \
                    or self.col_voltorbs[rand_ind[1]] == 5:
                rand_ind = (randint(0, 4), randint(0, 4))

            self.spaces[rand_ind] = 2
            self.row_points[rand_ind[0]] += 1
            self.col_points[rand_ind[1]] += 1

        # Place x3 multipliers on board
        for point in range(0, self.level_board[1]):

            rand_ind = (randint(0, 4), randint(0, 4))

            while rand_ind in self.spaces.keys() or self.row_voltorbs[rand_ind[0]] == 5 \
                    or self.col_voltorbs[rand_ind[1]] == 5:
                rand_ind = (randint(0, 4), randint(0, 4))

            self.spaces[rand_ind] = 3
            self.row_points[rand_ind[0]] += 2
            self.col_points[rand_ind[1]] += 2

    # Returns a list of the Voltorbs in each column
    def get_col_voltorbs(self):
        return self.col_voltorbs

    # Returns a list of the Voltorbs in each row
    def get_row_voltorbs(self):
        return self.row_voltorbs

    # Returns a list of the points in each column
    def get_col_points(self):
        return self.col_points

    # Returns a list of the points in each row
    def get_row_points(self):
        return self.row_points

    # Returns the value of a space on the board
    def check_space(self, space):
        if space in self.spaces.keys():
            return self.spaces[space]
        else:
            return 1


b = Board(1)
