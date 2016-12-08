'''
Created on 21 Nov 2016

@author: Sami Laine <sami.v.laine@gmail.com>
'''

class Othello:
    
    EMPTY = 0
    BLACK = -1
    WHITE = 1
    TIE = 0
    LIMIT = 8 # Amount of rows and columns in the board (0-7)
    DIRECTIONS = [[0, -1], [1, 0], [0, 1], [-1, 0],
                  [1, -1], [1, 1], [-1, 1], [-1, -1]]
    CHARACTERS = {}
    CHARACTERS[EMPTY] = "_"
    CHARACTERS[BLACK] = "M"
    CHARACTERS[WHITE] = "V"

    def __init__(self):
        self.__canvas = [[Othello.EMPTY] * Othello.LIMIT for i in range(Othello.LIMIT)]
        self.set_cell(int(Othello.LIMIT / 2) - 1, int(Othello.LIMIT / 2) - 1, Othello.BLACK)
        self.set_cell(int(Othello.LIMIT / 2),     int(Othello.LIMIT / 2),     Othello.BLACK)
        self.set_cell(int(Othello.LIMIT / 2) - 1, int(Othello.LIMIT / 2),     Othello.WHITE)
        self.set_cell(int(Othello.LIMIT / 2),     int(Othello.LIMIT / 2) - 1, Othello.WHITE)


    def tell_winner(self):
        whites = 0
        blacks = 0
        for y in range(Othello.LIMIT):
            for x in range(Othello.LIMIT):
                if self.get_cell(x, y) == Othello.WHITE:
                    whites += 1
                elif self.get_cell(x, y) == Othello.BLACK:
                    blacks += 1
        if whites == blacks: return Othello.TIE
        if whites > blacks: return Othello.WHITE
        return Othello.BLACK

    def check_placement(self, x, y, color, directions=[]):
        if self.out_of_bounds(x, y): return False

        if self.get_cell(x, y) != Othello.EMPTY:
            return False

        del directions[:]

        for direction in Othello.DIRECTIONS:
            dir_x = direction[0]
            dir_y = direction[1]
            i = 1
            while i <= Othello.LIMIT:
                check_x = x + dir_x * i
                check_y = y + dir_y * i
                if self.out_of_bounds(check_x + dir_x, check_y + dir_y): break
                if self.get_cell(check_x, check_y) == -color:
                    if self.get_cell(check_x, check_y, direction, 1) == color:
                        directions.append(direction)
                        break
                else:
                    break
                i += 1
        if len(directions) > 0:
            return True
        return False

    def can_place_piece(self, color):
        for y in range(Othello.LIMIT):
            for x in range(Othello.LIMIT):
                if self.check_placement(x, y, color): return True
        
        return False
    
    def add_piece(self, cell, color):
        x = cell[0]
        y = cell[1]
        if self.check_placement(x, y, color):
            self.turn(x, y, color)
            self.set_cell(x, y, color)
            return True
        else:
            return False
        
    def out_of_bounds(self, x, y):
        if x < 0 or y < 0 or x > Othello.LIMIT -1 or y > Othello.LIMIT -1:
            return True
        return False
    
    def get_cell(self, x, y, direction=[0,0], multiplier = 0):
        return self.__canvas[y + direction[1] * multiplier][x + direction[0] * multiplier]
    
    def set_cell(self, x, y, value = None):
        if value is None:
            value = self.EMPTY
        self.__canvas[y][x] = value

    def turn(self, x, y, color):
        directions = []
        if self.check_placement(x, y, color, directions):
            for direction in directions:
                i = 1
                dir_x = direction[0]
                dir_y = direction[1]
                while i < Othello.LIMIT:
                    turn_x = x + dir_x * i
                    turn_y = y + dir_y * i
                    if self.get_cell(x, y, direction, i) == color:
                        break
                    self.set_cell(turn_x, turn_y, color)
                    i += 1

    def get_character(self, x, y):
        return Othello.CHARACTERS[self.get_cell(x, y)]

    def __str__(self):
        board = "  "
        for i in range(Othello.LIMIT):
            board += "{:d} ".format(i)
        board += "\n"
        for y in range(Othello.LIMIT):

            line = str(y) + " "
            for x in range(Othello.LIMIT):
                line += self.get_character(x, y) + " "
            board += line + "\n"
        return board[:-1]
