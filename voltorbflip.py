import board


class Game:
    def __init__(self):
        self.total_coins = 0
        self.level_coins = 0
        self.level = 1
        self.board = board.Board(self.level)
        self.num_multipliers = self.board.get_num_multipliers()
        self.num_voltorbs = self.board.get_num_multipliers()
        self.total_multipliers = 0

    # Checks the space (x,y) for a multiplier or Voltorb and updates game status and coins.
    def check_space(self, space):
        result = self.board.check_space(space)
        status = ""
        if result > 1:
            self.total_multipliers += 1
            self.num_multipliers -= 1

            if self.level_coins == 0:
                self.level_coins += result
            else:
                self.level_coins *= result

                if self.num_multipliers == 0:
                    status = "Level Success"
        elif result == 0:
            self.total_coins += self.level_coins
            status = "Game Over"
        else:
            self.total_multipliers += 1
        space_result = (result, self.level_coins, self.total_coins, status)
        return space_result

    # Gets the value in a space
    def get_space(self, space):
        return self.board.check_space(space)

    # Makes a new game board
    def new_board(self):
        if self.num_multipliers == 0:
            self.level += 1
        elif self.total_multipliers < self.num_voltorbs:
            if self.total_multipliers == 0:
                self.level = 1
            elif self.total_multipliers < self.level:
                self.level = self.total_multipliers

        self.board = board.Board(self.level)
        self.level_coins = 0
        self.num_multipliers = self.board.get_num_multipliers()
        self.num_voltorbs = self.board.get_num_voltorbs()
        self.total_multipliers = 0

