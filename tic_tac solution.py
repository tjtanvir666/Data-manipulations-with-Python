import os
import random

def display_board(board):
    os.system('cls')
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] )
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

board = ["ignore 0 index",'x','x','x','o','o','o','x','x','x']
display_board(board)

def player_input():
    marker = ''
    while not (marker == 'x' or marker == 'o'):
        print(marker)
        marker = input("Player 1: What would you like? 'x' or 'o' ? ").lower()
        
    if (marker == 'x'):
        return ('x' , 'o') ##returning tuples
    else:
        return ('o' , 'x')
 
choice = player_input()
print(choice)    

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
win_check(board)    

def choose_first():
    if(random.randint(0,1) == 0):
        return "player 1"
    else:
        return "player 2"

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False  ## not full cuz space_check will return true 
        else:
            return True