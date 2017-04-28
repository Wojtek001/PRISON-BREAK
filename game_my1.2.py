import sys
import random
import os
import time
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_board():
              #1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
    board = [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','[',']','.','.','.','.','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','#',' ',' ',' ',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ','.','.','.',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#',' ',' ','.',' ',' ',' ',],\
             ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','[','.','.','.',' ',' ',' ',],\
             ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#',' ',' ',' ',' ',' ',' ',]]

    return board

def insert_player(board, y_axis, x_axis):
    board[y_axis][x_axis] = '@'

def print_board(board):
    for row in board:
        print("".join(row))

def main():
    life = 100

    backpack = ['key']
    chest_1 = ['key', 'piece_of_map_1', 'chocolate_bar']

    y_axis = 1
    x_axis = 1

    board = create_board()
    insert_player(board, y_axis, x_axis)
    print_board(board)


    while True:

        os.system('clear')
        print_board(board)

        print("Life: ", life)

        pressedkey = getch()   # 4 petle definiujace ruch postaci
        if pressedkey is 'w' or pressedkey is 'W':
            if board[y_axis-1][x_axis] is '.':
                board[y_axis][x_axis]='.'
                y_axis -=1
                insert_player(board, y_axis, x_axis)


        if pressedkey is 's' or pressedkey is 'S':
            if board[y_axis+1][x_axis] is '.':
                board[y_axis][x_axis]='.'
                y_axis +=1
                insert_player(board, y_axis, x_axis)


        if pressedkey is 'a' or pressedkey is 'A':
            if board[y_axis][x_axis-1] is '.':
                board[y_axis][x_axis]='.'
                x_axis -=1
                insert_player(board, y_axis, x_axis)


        if pressedkey is 'd' or pressedkey is 'D':
            if board[y_axis][x_axis+1] is '.':
                board[y_axis][x_axis]='.'
                x_axis +=1
                insert_player(board, y_axis, x_axis)


        if pressedkey is "q":
            break

        if pressedkey is 'b' or pressedkey is 'B':  # Ta opsja pozwala nam otworzyc plecak i nastepnie wraca do mapy
            os.system('clear')
            for items in backpack:
                print (items)


            #if pressedkey == 'm' or pressedkey is 'M':
                #print_board(board)


        if pressedkey == 'o' and (board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@'):
            print("You opened the chest and found a key and a chocolate bar. Now it's in your backpack")
            time.sleep(3)
            backpack.extend(chest_1)
            del chest_1[:]
            print(backpack)

        if pressedkey =='o' and backpack[0] == 'key' and  board[13][16] =='@':
            board[13][17] = '.'







main()
