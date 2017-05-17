import sys
import random
import os
import time
import tty
import termios
import csv

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_board(filename):

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        board = []
        for rows in reader:
            board.append(rows)

    return board

def insert_player(board, y_axis, x_axis):
    board[y_axis][x_axis] = '@'

def print_board(board):
    for row in board:
        print("".join(row))

def change_map(board):
    if board[13][16]:
        filename = "board_2.csv"
    return filename


def main():
    life = 100

    backpack = []
    chest_1 = ['key', 'piece_of_map_1', 'chocolate_bar']

    y_axis = 1
    x_axis = 1

    filename = "board_1.csv"

    board = create_board(filename)
    insert_player(board, y_axis, x_axis)


    while True:

        os.system('clear')
        print_board(board)

        print("Life: ", life)

        if len(backpack) == 0:
            print("BACKPACK: --- ")
        else:
            print("BACKPACK:\n",'\n'.join(backpack))


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


        if pressedkey == 'o':
            if board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@':
                if len(chest_1) > 0:
                    print("You opened the chest and found a key and a chocolate bar. Now it's in your backpack")
                    backpack.extend(chest_1)
                    del chest_1[:]
                    time.sleep(2)
                else:
                    print("EMPTY")
                    time.sleep(0.5)

            elif board[13][16] =='@' and backpack[0] == 'key'  :
                board[13][17] = '.'
                del backpack[0]

        if board[13][20] == '@':
            filename = "board_2.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)

        if filename =="board_2.csv" and board[16][33] == '@':
            filename = "board_3.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)


main()
