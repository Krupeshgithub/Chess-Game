import random
import numpy as np
from Conditions import comm_Condition
from Conditions import piece_Condtions

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
        
class Start_Game(Game):
    
    players = {
                "WHITE" : True,
                "BLACK" : False
            }
            
    def __init__ (self):
        Game.__init__(self)
        self.game()
        
    def start_game (self):
        
        print(self.chess)

        while True: 
                
                try:    
                    self.current_row = int(input("Enter current_row ::")) 
                    self.current_col = int(input("Enter current_col ::"))
                    self.next_row = int(input("Enter next_row ::"))
                    self.next_col = int(input("Enter next_col ::"))
                except Exception as e:
                   print(e) 
                   raise ValueError("Enter some value don't skip blank")
                
                if self.current_row == "50":
                    False
                
                else:

                    get_piece = self.chess[self.current_row,self.current_col]

                    comm_Condition.condition(self.current_row,self.current_col,self.next_row,self.next_col)

                    if (get_piece == piece_dict['WHITE']['Pawn']) or (get_piece == piece_dict['BLACK'] ['Pawn']):
                        piece_Condtions.pawn_Conditions(get_piece, piece_dict, self.chess, \
                                                        self.current_row,self.current_col, \
                                                        self.next_row, self.next_col)

                    elif (get_piece == piece_dict['WHITE']['Rook']) or (get_piece == piece_dict['BLACK'] ['Rook']):
                        piece_Condtions.rook_Conditions(piece_dict, self.chess, \
                                                        self.current_row,self.current_col, \
                                                        self.next_row, self.next_col)
                            
                    elif (get_piece == piece_dict['WHITE']['Knight']) or (get_piece == piece_dict['BLACK'] ['Knight']):
                        piece_Condtions.knight_Conditons(piece_dict, self.chess, \
                                                         self.current_row, self.current_col, \
                                                         self.next_row, self.next_col)
                    
                    elif (get_piece == piece_dict['WHITE']['Bishop']) or (get_piece == piece_dict['BLACK'] ['Bishop']):
                        piece_Condtions.bishop_Conditions(piece_dict, self.chess, \
                                                          self.current_row, self.current_col, \
                                                          self.next_row, self.next_col)
                           
                    elif (get_piece == piece_dict['WHITE']['King']) or (get_piece == piece_dict['BLACK'] ['King']):
                        piece_Condtions.king_Condtions(piece_dict, self.chess, \
                                                       self.current_row, self.current_col, \
                                                       self.next_row, self.next_col)
                    
                    elif (get_piece == piece_dict['WHITE']['Queen']) or (get_piece == piece_dict['BLACK'] ['Queen']):
                        piece_Condtions.queen_Conditions(piece_dict, self.chess, \
                                                         self.current_row, self.current_col, \
                                                         self.next_row, self.next_col)

                    else:
                        raise ValueError("Enter valid number's")

# llist.testing()

llist = Start_Game()
llist.start_game()
