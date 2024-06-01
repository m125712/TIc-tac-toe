import os
os.system("clear")
class Board:
    def __init__(self):
        self.cells =["-","-","-",
                     "-","-","-",
                     "-","-","-"
                     ]

    def refresh_page(self):
        os.system("clear")
        board.display()
    def display(self):
       print(self.cells[0],self.cells[1],self.cells[2])
       print("------")
       print(self.cells[3],self.cells[4],self.cells[5])
       print("------")
       print(self.cells[6],self.cells[7],self.cells[8])
       print("------")
    def update(self, player, position):
        if self.cells[position] == "-":
             self.cells[position] = player
    def is_wiinner(self, player):
        if self.cells[0] == player and self.cells[1] == player and self.cells[2] == player:
            return True
        elif self.cells[3] == player and self.cells[4] == player and self.cells[5] == player:
            return True
        elif self.cells[6] == player and self.cells[7] == player and self.cells[8] == player:
            return True
        elif self.cells[0] == player and self.cells[3] == player and self.cells[6] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[0] == player and self.cells[4] == player and self.cells[8] == player:
            return True
        elif self.cells[2] == player and self.cells[4]== player and self.cells[6]==player:
            return True
    def is_tie(self):
        if "-" not in self.cells:
            return True
       

board= Board()



while True:
    board.refresh_page()
    x_choice = int(input("X's choice: "))
    board.update("X", x_choice)
    if board.is_wiinner("X"):
        print("X wins!")
        break
    if(board.is_tie()):
        print("It's a tie!")
        break
    board.refresh_page()
    o_choice = int(input("O's choice: "))
    board.update("O", o_choice)
    if board.is_wiinner("O"):
        print("O wins!")
        break
    if(board.is_tie()):
        print("It's a tie!")
        break

