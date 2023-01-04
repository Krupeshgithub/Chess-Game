errors = {
    1 : "'0' row & '0' col not count!",
    2 : "Enter some value don't skip blank",
    3 : "Enter only <= 8",
    4 : "Select valid next number!"
}

def movements (chess,current_row,current_col,next_row,next_col):
    chess[next_row,next_col] = chess[current_row,current_col]
    chess[current_row,current_col] = '-'
    print(chess)

def condition(current_row, current_col, next_row, next_col):
    if current_row == 0 or next_col == 0:
        raise ValueError(errors[1])
    # if (current_col or current_row or next_col or next_row <= 8):
    #     raise ValueError(errors[3])
    if current_col == current_row == next_col == next_row:
        raise ValueError(errors[4])
    else:
        return True