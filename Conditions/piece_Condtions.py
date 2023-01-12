from Conditions import comm_Condition

DIE_PIECE_WHITE = []
DIE_PIECE_BLACK = []

errors = comm_Condition.errors

def knight_queen(current_row, current_col):
    move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    operation_Condition = list()

    for offset in move_offsets:
        col_offset, row_offset = offset
        operation_Condition.append(((current_row + col_offset), (current_col + row_offset)))    

    return operation_Condition

def same_Operations(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):
    if (chess[current_row, current_col] not in ["♞", "♘"]) and (jump_Condtions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col)) is None:

        if (chess[next_row,next_col] in piece_dict['BLACK'].values()) and (turn_ == True):
            DIE_PIECE_BLACK.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
        elif (chess[next_row,next_col] in piece_dict['WHITE'].values()) and (turn_ == False):
            DIE_PIECE_WHITE.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            if (chess[next_row,next_col] == '-'):
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                turn_ = False if turn_ else True
                print(errors[4])
                return turn_

    elif (chess[current_row, current_col] in ["♞", "♘"]):

        if (chess[next_row,next_col] in piece_dict['BLACK'].values()) and (turn_ == True):
            DIE_PIECE_BLACK.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
        elif (chess[next_row,next_col] in piece_dict['WHITE'].values()) and (turn_ == True):
            DIE_PIECE_WHITE.append(chess[next_row,next_col])
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            if (chess[next_row,next_col] == '-'):
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                turn_ = False if turn_ else True
                print(errors[4])
                return turn_
    else:
        turn_ = False if turn_ else True
        return turn_

def pawn_Conditions(get_piece, turn_, piece_dict, chess, current_row, current_col, next_row, next_col):

    if jump_Condtions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col) is None:

        if piece_dict['WHITE']['Pawn'] == get_piece:

            if current_row == next_row and \
                ((current_col + 1 == (next_col)) or \
                current_col + 2 == (next_col))\
                and (chess[next_row,next_col] == '-'):   
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)

            else:
                
                if (chess[next_row,next_col] in (piece_dict['BLACK'].values())) \
                    and (current_col+1 == next_col and ((current_row+1 == (next_row)) or ((current_row-1) == (next_row)))):
        
                    DIE_PIECE_BLACK.append(chess[next_row,next_col])
                    comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
                
                else:
                    turn_ = False if turn_ else True
                    print(errors[4])
                    return turn_
        
        else:
            
            if current_row == next_row and ((current_col - 1 == (next_col)) or \
                current_col - 2 == (next_col))\
                and (chess[next_row,next_col] == '-'):

                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                
                if (chess[next_row,next_col] in (piece_dict['WHITE'].values())) \
                    and (current_col-1 == next_col and ((current_row+1 == (next_row)) or ((current_row-1) == (next_row)))):
                    
                    DIE_PIECE_WHITE.append(chess[next_row,next_col])
                    comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
                
                else:
                    turn_ = False if turn_ else True
                    print(errors[4])
                    return turn_
    else:
        turn_ = False if turn_ else True
        return turn_

def rook_Conditions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):
    
    if (current_row == next_row) or (current_col == next_col):
        value = same_Operations(turn_, piece_dict, chess, current_row, current_col, next_row, next_col)
        return value
    
    else:
        turn_ = False if turn_ else True
        print(errors[4])
        return turn_

def king_Condtions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):

    if (current_row+1 == next_row) or (current_row-1 == next_row)\
             or (current_col+1 == next_col) or (current_col-1 == next_col):
        value = same_Operations(turn_, piece_dict, chess, current_row, current_col, next_row, next_col)
        return value

    else:
        turn_ = False if turn_ else True
        print(errors[4])
        return turn_

def bishop_Conditions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):
    
    current_plus = int(current_col + current_row)
    current_negative = int(current_col - current_row)
    next_plus = next_col + next_row
    next_negative = next_col - next_row

    if (current_plus == next_plus) or (current_negative == next_negative):
        value = same_Operations(turn_, piece_dict, chess, current_row, current_col, next_row, next_col)
        return value

    else:
        turn_ = False if turn_ else True
        print(errors[4])
        return turn_
        
def knight_Conditons(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):

    if (next_row, next_col) in knight_queen(current_row, current_col):
        value = same_Operations(turn_, piece_dict, chess, current_row, current_col, next_row, next_col)
        return value

    else:
        turn_ = False if turn_ else True
        print(errors[4])
        return turn_
    
def queen_Conditions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):

    if (next_row, next_col) not in knight_queen(current_row, current_col):
        value = same_Operations(turn_, piece_dict, chess, current_row, current_col, next_row, next_col)
        return value

    else:
        turn_ = False if turn_ else True
        print(errors[4])
        return turn_

def jump_Condtions(turn_, piece_dict, chess, current_row, current_col, next_row, next_col):

    if current_row > next_row and current_col == next_col:
        for i in range(current_row-next_row):
            if chess[(current_row-i), next_col] != '-' and i!=0:
                print(errors[5])
                return False

    elif current_row < next_row and current_col == next_col:
        for i in range(next_row-current_row):
            if chess[(current_row+i), next_col] != '-' and i!=0:
                print(errors[5])
                return False
     
    elif current_row == next_row and current_col > next_col:
        for i in range(current_col-next_col):
            if chess[(current_row, (current_col-i))] != '-' and i!=0:
                print(errors[5])
                return False
     
    elif current_row == next_row and current_col < next_col:
        for i in range(next_col-current_col):
            if chess[(current_row, (current_col+i))] != '-' and i!=0:
                print(errors[5])
                return False
     

    elif current_row < next_row and current_col > next_col:
        for i in range(next_row - current_row):
            if chess[(current_row+i), (current_col-i)] != '-' and i!=0:
                print(errors[5])
                return False

    elif current_row > next_row and current_col < next_col:
        for i in range(current_row - next_row):
            if chess[(current_row-i), (current_col+i)] != '-' and i!=0:
                print(errors[5])
                return False
        
    elif current_row > next_row and current_col > next_col:
        for i in range(current_row - next_row):
            if chess[(current_row+i), (current_col+i)] != '-' and i!=0:
                print(errors[5])
                return False
 
    elif current_row < next_row and current_col < next_col:
        for i in range(next_row - current_row):
            if chess[(current_row-i), (current_col-i)] != '-' and i!=0:
                print(errors[5])
                return False
