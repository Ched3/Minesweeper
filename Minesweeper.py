import random
import numpy as np

class Minesweeper:

    def __init__(self, width, height, bombs):
        self.width = width
        self.height = height
        self.bombs = bombs
        self.board = np.zeros((width, height))
        self.playerBoard = np.full((width, height), "")

    def description(self):
        return f"The board is {self.width} tiles long and {self.height} tiles high with {self.bombs} bombs"

    def placeBomb(self):
        bombs_placed = 0
        while bombs_placed < self.bombs:
            randomX = random.randint(0, self.width - 1)
            randomY = random.randint(0, self.height - 1)
            if self.board[randomX][randomY] != -1:
                self.board[randomX][randomY] = -1
                bombs_placed += 1
        return self.board

    def placeNumbers(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] != -1:
                    self.board[i][j] = self.adjacentBombs(i, j)

    def adjacentBombs(self, x, y):
        adjacent_bombs = 0
        for i in range(max(0, x - 1), min(self.width, x + 2)):
            for j in range(max(0, y - 1), min(self.height, y + 2)):
                if self.board[i][j] == -1:
                    adjacent_bombs += 1
        return adjacent_bombs

    def reveal(self, x, y):
        if self.playerBoard[x][y] != "":
            return False

        stack = [(x, y)]

        while stack:
            i, j = stack.pop()
            if self.board[i][j] == -1:
                return True
            if self.board[i][j] == 0:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        new_x, new_y = i + dx, j + dy
                        if 0 <= new_x < self.width and 0 <= new_y < self.height and self.playerBoard[new_x][
                            new_y] == "":
                            self.playerBoard[new_x][new_y] = self.board[new_x][new_y]
                            if self.board[new_x][new_y] == 0:
                                stack.append((new_x, new_y))
        return False

    def flag(self, x, y):
        if self.playerBoard[x][y] == "":
            self.playerBoard[x][y] = "F"

    def checkWin(self):
        # You win if all non-bomb cells have been revealed
        return (self.playerBoard == "").sum() == self.bombs and (self.playerBoard == "F").sum() == 0

    def printBoard(self):
        return self.board

    def __str__(self):
        return f"Width: {self.width} Height: {self.height} bombs: {self.bombs}"