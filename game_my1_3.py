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

#--------------------------------------BACKPACK--------------------------------
def display_inventory(inventory):
    total_items = 0
    for key in inventory:
        print(key, ':', inventory[key])
        total_items += inventory[key]
    print(''*80)
    print("Total number of items: ", total_items)
#dodaje listę elementów do aktualnego inventory
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return(inventory)


def main():
    points = 100

    inventory = {}
    chest_1 = ['key_1','key_2','key_3', 'piece_of_map_1', 'chocolate_bar']
    chest_2 = ['key_2', 'piece_of_map_1', 'chocolate_bar']
    chest_3 = ['key_3', 'piece_of_map_1', 'chocolate_bar']
    chest_4 = ['key_4', 'piece_of_map_1', 'chocolate_bar']

    y_axis = 1
    x_axis = 1

    filename = "board_1.csv"

    board = create_board(filename)
    insert_player(board, y_axis, x_axis)


    while True:

        os.system('clear')
        print_board(board)

        print("Points: ", points)

        display_inventory(inventory)

        pressedkey = getch()   # 4 petle definiujace ruch postaci
        if pressedkey is 'w' or pressedkey is 'W':
            if board[y_axis-1][x_axis] is '-':
                points -= 10
                board[y_axis][x_axis]='.'
                y_axis -=1
                insert_player(board, y_axis, x_axis)
                continue
            if board[y_axis-1][x_axis] is '.' and '-':
                board[y_axis][x_axis]='.'
                y_axis -=1
                insert_player(board, y_axis, x_axis)

        if pressedkey is 's' or pressedkey is 'S':
            if board[y_axis+1][x_axis] is '-':
                points -= 10
                board[y_axis][x_axis]='.'
                y_axis +=1
                insert_player(board, y_axis, x_axis)
                continue
            if board[y_axis+1][x_axis] is '.':
                board[y_axis][x_axis]='.'
                y_axis +=1
                insert_player(board, y_axis, x_axis)

        if pressedkey is 'a' or pressedkey is 'A':
            if board[y_axis][x_axis-1] is '-':
                points -= 10
                board[y_axis][x_axis]='.'
                x_axis -=1
                insert_player(board, y_axis, x_axis)
                continue
            if board[y_axis][x_axis-1] is '.':
                board[y_axis][x_axis]='.'
                x_axis -=1
                insert_player(board, y_axis, x_axis)

        if pressedkey is 'd' or pressedkey is 'D':
            if board[y_axis][x_axis+1] is '-':
                points -= 10
                board[y_axis][x_axis]='.'
                x_axis +=1
                insert_player(board, y_axis, x_axis)
                continue
            if board[y_axis][x_axis+1] is '.':
                board[y_axis][x_axis]='.'
                x_axis +=1
                insert_player(board, y_axis, x_axis)


        if pressedkey is "q":
            break


        if pressedkey == 'o':
            #otwieranie 1 skrzynki
            if board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@':
                if len(chest_1) > 0:
                    print("You opened the chest and found a key and a chocolate bar. Now it's in your backpack")
                    add_to_inventory(inventory, chest_1)
                    del chest_1[:]
                    time.sleep(2)
                else:
                    print("EMPTY")
                    time.sleep(0.5)
            #otwieranie 1 skrzynki
            elif board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@':
                if len(chest_1) > 0:
                    print("You opened the chest and found a key and a chocolate bar. Now it's in your backpack")
                    add_to_inventory(inventory, chest_1)
                    del chest_1[:]
                    time.sleep(2)
                else:
                    print("EMPTY")
                    time.sleep(0.5)
            #otwieranie 1 skrzynki
            elif board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@':
                if len(chest_1) > 0:
                    print("You opened the chest and found a key and a chocolate bar. Now it's in your backpack")
                    add_to_inventory(inventory, chest_1)
                    del chest_1[:]
                    time.sleep(2)
                else:
                    print("EMPTY")
                    time.sleep(0.5)
            #otwieranie 1 skrzynki
            elif board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@':
                if len(chest_1) > 0:
                    print("You opened the chest and found a key and a chocolate bar. Now it's in your backpack")
                    add_to_inventory(inventory, chest_1)
                    del chest_1[:]
                    time.sleep(2)
                else:
                    print("EMPTY")
                    time.sleep(0.5)
#******************************OTWIERANIE DRZWI*********************************
            #otwieranie drzwi na 1 mapie
            elif board[13][16] =='@' and 'key_1' in inventory :
                board[13][17] = '.'
                del inventory['key_1']
            #otwieranie drzwi na 2 mape z korytarza
            elif board[11][26] =='@':
                board[11][27] = '.'
            #otwieranie drzwi na 2 mapie
            elif board[13][33] =='@' and 'key_2' in inventory :
                board[14][33] = '.'
                del inventory['key_2']
            #otwieranie drzwi na 3 mape z korytarza
            elif board[22][35] =='@':
                board[23][35] = '.'
            #otwieranie drzwi na 3 mapie
            elif board[36][27] =='@' and 'key_3' in inventory :
                board[36][26] = '.'
                del inventory['key_3']
            #otwieranie drzwi na 4 mape z korytarza
            elif board[34][18] =='@':
                board[34][17] = '.'


        if filename == "board_1.csv" and board[11][20] == '@':
            filename = "board_2.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)

        if filename =="board_2.csv" and board[16][33] == '@':
            filename = "board_3.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)


main()
