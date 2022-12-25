import random
import numpy as np

piece_dict = {"WHITE" : {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" },\
 "BLACK" : {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }}

class Structure:

    abc = ['S','a','b','c','d','e','f','g']

    def __init__ (self):
        chess = np.zeros(shape=(8,8),dtype = 'object')
        for i in range(0,8):
            chess[0,i] = i
        count = 0
        for i in self.abc:
            chess[count,0] = i
            count+=1
        count = 1
        for i in range(0,len(self.abc)):
            chess[count,1] = piece_dict["WHITE"]["Pawn"]
            count+=1
        print(chess)

Structure()