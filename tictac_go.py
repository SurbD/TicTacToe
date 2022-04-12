from tkinter import *


class Tictactoe:

    def __init__(self):

        self.root = Tk()

        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        self.entry_b = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        self.player = 'X'
        self.stop_game = False

        # self.run()

    def __callback(self,r,c):
    
        if self.player == 'X' and self.entry_b[r][c] == 0 and self.stop_game == False:
            self.board[r][c].configure(text='X', bg='white', fg='red')
            self.entry_b[r][c] = 'X'
            self.player = 'O'

        if self.player == 'O' and self.entry_b[r][c] == 0 and self.stop_game == False:
            self.board[r][c].configure(text='O', bg='white', fg='blue')
            self.entry_b[r][c] = 'O'
            self.player = 'X'

        print(tk_.entry_b)      
        self.__check_winner()


    def __check_winner(self):
        """ Description...."""

        for c in range(3):
            if self.entry_b[0][c] == self.entry_b[1][c] == self.entry_b[2][c] != 0:
                self.board[0][c].configure(bg='grey')
                self.board[1][c].configure(bg='grey')
                self.board[2][c].configure(bg='grey')
                self.stop_game = True

        for r in range(3):
            if self.entry_b[r][0] == self.entry_b[r][1] == self.entry_b[r][2] != 0:
                self.board[r][0].configure(bg='grey')
                self.board[r][1].configure(bg='grey')
                self.board[r][2].configure(bg='grey')
                self.stop_game= True

        if self.entry_b[0][0] == self.entry_b[1][1] == self.entry_b[2][2] != 0:
            self.board[0][0].configure(bg='grey')
            self.board[1][1].configure(bg='grey')
            self.board[2][2].configure(bg='grey')
            self.stop_game = True
            
        if self.entry_b[0][2] == self.entry_b[1][1] == self.entry_b[2][0] != 0:
            self.board[0][2].configure(bg='grey')
            self.board[1][1].configure(bg='grey')
            self.board[2][0].configure(bg='grey')
            self.stop_game = True

    def run(self):
    
        for i in range(3):
            for j in range(3):
                self.board[i][j] = Button(font=('Verdana', 18, 'bold'), width=3, height=2, command=lambda r=i,c=j: self.__callback(r,c))
                self.board[i][j].grid(row=i, column=j)

tk_ = Tictactoe()
tk_.run()
# print(tk_.board)
mainloop()

