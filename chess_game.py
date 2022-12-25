import random
import numpy as np
import ast

piece_dict = {"WHITE" : {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" },\
 "BLACK" : {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }}

class Structure:

    abc = ['S','a','b','c','d','e','f','g','h']

    def __init__ (self):
        self.chess = np.zeros(shape=(9,9),dtype = 'str')
        
        for i in range(0,9):
            self.chess[0,i] = i
        
        count = 0
        for i in self.abc:
            self.chess[count,0] = i
            count+=1
        

class Game(Structure):

    def __init__ (self):
        Structure.__init__(self)


    def game(self):
        count = 1
        temp = 1
        val = 3
        for i in range(0,len(self.abc)-1):
            self.chess[count,2] = piece_dict["WHITE"]["Pawn"]
            self.chess[count,7] = piece_dict["BLACK"]["Pawn"]
            self.chess[count,3] = '-'
            self.chess[count,4] = '-'
            self.chess[count,6] = '-'
            self.chess[count,5] = '-'
            
            if temp <= 5:
                self.chess[count,1] = list(piece_dict["WHITE"].values())[temp]
                self.chess[count,8] = list(piece_dict["BLACK"].values())[temp]

            else:
                self.chess[count,1] = list(piece_dict["WHITE"].values())[val]
                self.chess[count,8] = list(piece_dict["BLACK"].values())[val]

                val-=1
                
            count+=1
            temp+=1
        print(self.chess)
        
class Start_Game(Game):
    
    def __init__ (self,current_row,current_col,next_row,next_col):
        self.current_row = current_row
        self.current_col = current_col
        self.next_row = next_row
        self.next_col = next_col
        Game.__init__(self)
        self.game()
        self.__prev_game = self.chess
    
    def start_game (self):
        var = self.__prev_game[self.current_row,self.current_col]
        self.__prev_game[self.next_row,self.next_col] = var
        self.__prev_game[self.current_row,self.current_col] = '-'
        print(self.__prev_game)
        

inp = input("Enter the number please :: ",)
input = tuple([int(i) for i in inp])
status = True
while status:
    if inp != 'quit':
        obj = Start_Game(input)
        obj.start_game()
    else:
        break