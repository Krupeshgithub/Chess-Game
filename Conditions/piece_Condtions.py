from Conditions import comm_Condition

DIE_PIECE_WHITE = []
DIE_PIECE_BLACK = []

errors = comm_Condition.errors

def pawn_Conditions(piece_dict, chess, current_row, current_col, next_row, next_col):

    if piece_dict['WHITE']['Pawn']:

        if current_row == next_row and \
            ((current_col + 1 == (next_col)) or \
            current_col + 2 == (next_col))\
            and (chess[next_row,next_col] == '-'):   

            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)

        else:
            
            if (chess[next_row,next_col] == any(piece_dict['BLACK'].values())) \
                and (current_col+1,current_row+1) == (next_col,next_row):

                DIE_PIECE_BLACK.append(chess[next_row,next_col])
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                print(ValueError(errors[4]))
    
    else:
        
        if current_row == next_row and ((current_col + 1 == (next_col)) or \
            current_col + 2 == (next_col))\
            and (chess[next_row,next_col] == '-'):

            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            
            if (chess[next_row,next_col] == any(piece_dict['WHITE'].values())) \
                and (current_col-1,current_row-1) == (next_col,next_row):
                
                DIE_PIECE_WHITE.append(chess[next_row,next_col])
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                print(ValueError(errors[4]))

def rook_Conditions(piece_dict, chess, current_row, current_col, next_row, next_col):
    
    if (current_row == next_row) or (current_col == next_col):
        
        if (chess[next_row,next_col] == any(piece_dict['BLACK'].values())):
            DIE_PIECE_BLACK.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        elif (chess[next_row,next_col] == any(piece_dict['WHITE'].values())):
            DIE_PIECE_WHITE.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            if (chess[next_row,next_col] == '-'):
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                print(ValueError(errors[4]))

    else:
        print(ValueError(errors[4]))

def king_Condtions(piece_dict, chess, current_row, current_col, next_row, next_col):

    if ((current_row+1 or current_row-1) == next_row)\
        or ((current_col+1 or current_col-1) == next_col):

        if (chess[next_row,next_col] == any(piece_dict['BLACK'].values())):
            DIE_PIECE_BLACK.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        elif (chess[next_row,next_col] == any(piece_dict['WHITE'].values())):
            DIE_PIECE_WHITE.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            if (chess[next_row,next_col] == '-'):
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                print("hgello brother")
                print(ValueError(errors[4]))
    else:
        print(ValueError(errors[4]))
