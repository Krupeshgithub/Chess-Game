import random
import numpy as np

piece_dict = {"WHITE" : {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" },\
 "BLACK" : {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }}

class Structure:

    abc = ['S','a','b','c','d','e','f','g','h']

    def __init__ (self):
        chess = np.zeros(shape=(9,8),dtype = 'str')
        for i in range(0,8):
            chess[0,i] = i
        count = 0
        for i in self.abc:
            chess[count,0] = i
            count+=1
        count = 1
        temp = 1
        for i in range(0,len(self.abc)-1):
            chess[count,2] = piece_dict["WHITE"]["Pawn"]
            if temp <= 5:
                chess[count,1] = list(piece_dict["WHITE"].values())[temp]
            chess[count,6] = piece_dict["BLACK"]["Pawn"]
            count+=1
            temp+=1
        count = 1
        print(chess)

Structure()