'''
Created on 28 Nov 2016

@author: Sami Laine <sami.v.laine@gmail.com>
'''
from tkinter import *
from othello import Othello
from othellowindow import OthelloWindow

class PlayOthello:
    def __init__(self):
        self.__tk = Tk()
        self.__game = Othello()
        self.__w = OthelloWindow(Othello.LIMIT, self.__tk, self.__game)
        self.__tk.title("Othello")
        self.__turn = Othello.BLACK
        self.__tk.bind("<Button-1>", self.click)
        self.__tk.bind("<Motion>", self.motion)
        self.__w.draw_board(self.__game)
        self.__mouse_x = 0
        self.__mouse_y = 0
        self.__square_id = 0

        self.__tk.mainloop()

    def click(self, event):
        x, y =self.__w.get_tile(event.x, event.y)
        cell = [x, y]
        self.play_turn(cell)
        if not self.__game.can_place_piece(Othello.BLACK) or not self.__game.can_place_piece(Othello.WHITE):
            self.end_game()

        self.__w.draw_board(self.__game, self.__turn)

    def motion(self, event):
        x, y = self.__w.get_tile(event.x, event.y)

        if x == self.__mouse_x and y == self.__mouse_y:
            return False

        self.__w.update_tile(x, y)
        #self.__tk.title("Othello x:{:d} y:{:d}".format(self.__mouse_x, self.__mouse_y))
        self.__mouse_x, self.__mouse_y = x, y

    def play_turn(self, cell):
        if self.__game.add_piece(cell, self.__turn):
            if self.__game.can_place_piece(-self.__turn):
                self.__turn = -self.__turn
    
    def end_game(self):
        winner = self.__game.tell_winner()
        self.__w.draw_end(self.__game, winner)

        self.__tk.unbind("<Button-1>")
        self.__tk.unbind("<Motion>")
        self.__tk.mainloop()
