'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    print("\n\n")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def get_coord(square_num):
    if not(1 <= square_num <= 9): pass
    row = (square_num - 1) // 3
    col = (square_num - 1) % 3
    coord = [row, col]
    return coord

def put_in_board(board, mark, square_num):
    coord = get_coord(square_num)
    board[coord[0]][coord[1]] = mark

def get_free_squares(board):
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_squares.append([i, j])
    return free_squares

def make_random_move(board, mark):
    free_squares = get_free_squares(board)
    move = int(len(free_squares) * random.random())
    if free_squares != []: board[free_squares[move][0]][free_squares[move][1]] = mark

def is_empty(board, square_num):
    if not(1 <= square_num <= 9): return False
    coord = get_coord(square_num)
    return board[coord[0]][coord[1]] == " "

def is_row_all_marks(board, row_i, mark):
    return board[row_i][0] == mark and board[row_i][1] == mark and board[row_i][2] == mark

def is_col_all_marks(board, col_i, mark):
    return board[0][col_i] == mark and board[1][col_i] == mark and board[2][col_i] == mark

def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark): return True
        if is_col_all_marks(board, i, mark): return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark: return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark: return True
    return False

def make_best_move(board, mark):
    free_squares = get_free_squares(board)
    for i in range(len(free_squares)):
        board[free_squares[i][0]][free_squares[i][1]] = mark
        if is_win(board, mark): 
            print("best move found at " + str(free_squares[i]))
            print("\n")
            return
        board[free_squares[i][0]][free_squares[i][1]] = " "

    for i in range(len(free_squares)):
        board[free_squares[i][0]][free_squares[i][1]] = "X"
        if is_win(board, "X"):
            board[free_squares[i][0]][free_squares[i][1]] = mark
            print("preventing win at " + str(free_squares[i]))
            print("\n")
            return
        board[free_squares[i][0]][free_squares[i][1]] = " "    
    
    print("no significant moves")
    print("\n")
    make_random_move(board, mark)

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    while get_free_squares(board) != []:
        if not is_win(board, "O"):
            while True:
                user_input_x = input("Enter your move: ")
                square_num_x = int(user_input_x)
                
                if is_empty(board, square_num_x): break
                print("invalid move, try again")

            put_in_board(board, "X", square_num_x)
            print_board_and_legend(board)
        else:
            print("O wins")
            break
        
        if not is_win(board, "X"):
            make_best_move(board, "O")
            # make_random_move(board, "O")
            print_board_and_legend(board)
        else:
            print("X wins")
            break

