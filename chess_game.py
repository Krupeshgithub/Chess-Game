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
    
    def __init__ (self):
        Game.__init__(self)
        self.game()
        
    def start_game (self):
        print(self.chess)
        turn_ = 1
        while True: 
            if ("♔" in piece_Condtions.DIE_PIECE_WHITE and turn_ == 0): 
                print("🥳 Congrats you win!")
                break
            elif ("♚" in piece_Condtions.DIE_PIECE_BLACK and turn_ == 1): 
                print("🥳 Congrats you win!")
                break                
            try:
                print('WHITE') if turn_ else print('BLACK')
                self.current_row = int(input("Enter current_row ::")) 
                self.current_col = int(input("Enter current_col ::"))
                self.next_row = int(input("Enter next_row ::"))
                self.next_col = int(input("Enter next_col ::"))
            except ValueError as e:
                print("Enter some value don't skip blank")
                continue
            
            comm_Condition.condition(self.current_row,self.current_col,self.next_row,self.next_col)
            
            get_piece = self.chess[self.current_row,self.current_col]

            if (turn_ and get_piece in (piece_dict['WHITE'].values())) or (turn_ == 0 and get_piece in (piece_dict['BLACK'].values())):   

                turn_ = False if turn_ else True

                if (get_piece == piece_dict['WHITE']['Pawn']) or (get_piece == piece_dict['BLACK'] ['Pawn']):
                    value = piece_Condtions.pawn_Conditions(get_piece, turn_, piece_dict, self.chess, \
                                                            self.current_row,self.current_col, \
                                                            self.next_row, self.next_col)
                    if value is not None : turn_ = value

                elif (get_piece == piece_dict['WHITE']['Rook']) or (get_piece == piece_dict['BLACK'] ['Rook']):
                    value = piece_Condtions.rook_Conditions(turn_, piece_dict, self.chess, \
                                                            self.current_row,self.current_col, \
                                                            self.next_row, self.next_col)
                    if value is not None : turn_ = value

                elif (get_piece == piece_dict['WHITE']['Knight']) or (get_piece == piece_dict['BLACK'] ['Knight']):
                    value = piece_Condtions.knight_Conditons(turn_, piece_dict, self.chess, \
                                                            self.current_row, self.current_col, \
                                                            self.next_row, self.next_col)
                    if value is not None : turn_ = value
                
                elif (get_piece == piece_dict['WHITE']['Bishop']) or (get_piece == piece_dict['BLACK'] ['Bishop']):
                    value = piece_Condtions.bishop_Conditions(turn_, piece_dict, self.chess, \
                                                            self.current_row, self.current_col, \
                                                            self.next_row, self.next_col)
                    if value is not None : turn_ = value
                        
                elif (get_piece == piece_dict['WHITE']['King']) or (get_piece == piece_dict['BLACK'] ['King']):
                    value = piece_Condtions.king_Condtions(turn_, piece_dict, self.chess, \
                                                            self.current_row, self.current_col, \
                                                            self.next_row, self.next_col)
                    if value is not None : turn_ = value
                
                elif (get_piece == piece_dict['WHITE']['Queen']) or (get_piece == piece_dict['BLACK'] ['Queen']):
                    value = piece_Condtions.queen_Conditions(turn_, piece_dict, self.chess, \
                                                            self.current_row, self.current_col, \
                                                            self.next_row, self.next_col)
                    if value is not None : turn_ = value

                else:
                    raise ValueError("Enter valid number's")
            
            else:
                continue

# llist.testing()
llist = Start_Game()
llist.start_game()
