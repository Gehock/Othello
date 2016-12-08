'''
Created on 28 Nov 2016

@author: Sami Laine <sami.v.laine@gmail.com>
'''
from tkinter import *
from othello import *
from math import floor

class OthelloWindow:
    
    SIZE_MULTIPLIER = 50
    COLORS = {}
    COLORS[Othello.BLACK] = "black"
    COLORS[Othello.WHITE] = "white"
    COLORS[Othello.EMPTY] = "green"
    BOARD_X = 1
    BOARD_Y = 2
    
    def __init__(self, board_size, tk, game):
        self.__main_window = tk
        self.__board_size = board_size
        self.__game = game

        self.__main_window.title("Othello")
        self.__main_window.geometry("{0}x{1}".format((self.__board_size + 2) * OthelloWindow.SIZE_MULTIPLIER + 3,
                                                     (self.__board_size + 3) * OthelloWindow.SIZE_MULTIPLIER + 3))
        self.__canvas = Canvas(self.__main_window, \
                              width = (self.__board_size + 1) * OthelloWindow.SIZE_MULTIPLIER,
                              height = (self.__board_size + 3) * OthelloWindow.SIZE_MULTIPLIER, background = "lightgreen")
        self.__square_id = self.__canvas.create_rectangle(0,0,0,0)
        self.__canvas.pack(fill=BOTH)
        
        self.__tile_x = 0
        self.__tile_y = 0

    def draw_board(self, game, turn=None):
        self.__canvas.delete("all")
        if turn == Othello.WHITE:
            turn_string = "White"
        else:
            turn_string = "Black"
        self.heading("{:s}'s turn".format(turn_string))
        
        self.update_tile()
        self.draw_tiles(game)

    def draw_tiles(self, game):
        for y in range(self.__board_size):
            for x in range(self.__board_size):
                self.draw_cell(x, y, game.get_cell(x, y))

        for i in range(1, self.__board_size + 1):
            self.__canvas.create_text(OthelloWindow.SIZE_MULTIPLIER / 2,
                                      (i + 1.5) * OthelloWindow.SIZE_MULTIPLIER, text = i)
            self.__canvas.create_text((i + 0.5) * OthelloWindow.SIZE_MULTIPLIER,
                                      OthelloWindow.SIZE_MULTIPLIER * 1.5, text = i)

    def draw_end(self, game, winner):
        self.__canvas.delete("all")
        if winner == Othello.WHITE:
            string = "White wins"
        elif winner == Othello.BLACK:
            string = "Black wins"
        else:
            string = "It's a tie"
        
        self.heading(string)
        
        self.draw_tiles(game)

    def heading(self, string):
        self.__canvas.create_text(OthelloWindow.SIZE_MULTIPLIER * 0.5,
                          OthelloWindow.SIZE_MULTIPLIER * 0.5, text = string,
                          font = ('Helvetica', '16', 'bold'), anchor = W)

    def draw_cell(self, x, y, color):
        x1, y1, x2, y2 = self.tile_coordinates(x, y)
        self.__canvas.create_rectangle(x1, y1, x2, y2, \
                                    fill = OthelloWindow.COLORS[Othello.EMPTY])
        if color != Othello.EMPTY:
            self.__canvas.create_oval(x1, y1, x2, y2, \
                                    fill = OthelloWindow.COLORS[color])

    def update_tile(self, x = None, y = None):
        if x is None or y is None or self.__game.out_of_bounds(x, y):
            x = self.__tile_x
            y = self.__tile_y
        else:
            self.__tile_x = x
            self.__tile_y = y

        self.__canvas.delete(self.__square_id)
        x1, y1, x2, y2 = self.tile_coordinates(x, y)
        self.__square_id = self.__canvas.create_rectangle(x1, y1, x2, y2, \
                                    outline = OthelloWindow.COLORS[Othello.WHITE])

    def get_tile(self, x, y):
        x = floor((x - 2) / OthelloWindow.SIZE_MULTIPLIER - self.BOARD_X)
        y = floor((y - 2) / OthelloWindow.SIZE_MULTIPLIER - self.BOARD_Y)
        return x, y

    def tile_coordinates(self, x, y):
        x1 = (x + self.BOARD_X)     * OthelloWindow.SIZE_MULTIPLIER + 2
        y1 = (y + self.BOARD_Y)     * OthelloWindow.SIZE_MULTIPLIER + 2
        x2 = (x + self.BOARD_X + 1) * OthelloWindow.SIZE_MULTIPLIER
        y2 = (y + self.BOARD_Y + 1) * OthelloWindow.SIZE_MULTIPLIER
        return x1, y1, x2, y2
