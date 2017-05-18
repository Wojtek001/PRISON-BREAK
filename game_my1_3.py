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
#SPRAWDZIC CZY NIE SKASOWAC TEJ FUNKCJI
def change_map(board):
    if board[13][16]:
        filename = "board_2.csv"
    return filename
#_---------------------------------------
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

def print_table(inventory, order=None):

    sorted_inventory = []
    total_items = 0
    #sprawdza długość najdłuższego słowa w słowniku
    length = []
    for element in inventory:
        length.append(len(element))
    space = int(max(length)+3)

    #wyświetla tabelę 1 - od najmniejszego do największego, 2 - od największego do najmniejszego
    #nic - losowo
    print('{:>{width}} {:>{width}}'.format("item name","count", width = space))
    #wyrównuje do prawej {szerokość kolumny} x2 - 2 kolumny .format (co ma być w kolumnach , wartość-szerokości)
    print("-"*space*2)
    if order == 1:
        sorted_inventory = sorted(inventory.items(), key=lambda x:x[1], reverse=False)
        for element in sorted_inventory:
            print('{:>{width}} {:>{width}}'.format(element[0], element[1], width = space))
    elif order == 2:
        sorted_inventory = sorted(inventory.items(), key=lambda x:x[1], reverse=True)
        for element in sorted_inventory:
            print('{:>{width}} {:>{width}}'.format(element[0], element[1], width = space))
    else:
        for element in inventory:
            print('{:>{width}} {:>{width}}'.format(element, inventory[element], width = space))



#****************WŁĄCZANIE MODUŁÓW
def start_screen():
    import game_comp
    game_comp.main()

def lose_game():
    import end_screen_lose
    end_screen_lose.end_screen()


def first_game():
    import mini_hang
    mini_hang.hang_main()


def second_game():
    import zagadki
    zagadki.riddle()


def third_game():
    import roll_dice
    roll_dice.dice_main()


def guards_main(inventory,board):

    print('''
            \\\|||///               \\\|||///                \\\|||///
            .  =======              .  =======               .  =======
           / \| O   O |            / \| O   O |             / \| O   O |
           \ /  \v_'/              \ /  \v_'/               \ /  \v_'/
            #   _| |_               #   _| |_                #   _| |_
           (#) (     )             (#) (     )              (#) (     )
            #\//|* *|\\             #\//|* *|\\              #\//|* *|\\
            #\/(  *  )/             #\/(  *  )/              #\/(  *  )/
            #   =====               #   =====                #   =====
            #   (\ /)               #   (\ /)                #   (\ /)
            #   || ||               #   || ||                #   || ||
           .#---'| |----.          .#---'| |----.           .#---'| |----.
            #----' -----'           #----' -----'            #----' -----'
    
    
    If you have 5 gold coins you can pass, else you have to play our game to go away!
    
    ''')

    answer = input('Press p to pay or any other key to play the game: ').lower()

    if answer == 'p' and inventory['goldcoin'] > 4:
        board[44][10] = '.'
    else:
        final_game()

    import end_screen_win
    end_screen_win.end_screen

def final_game():
    import dojo_warm_hot
    dojo_warm_hot.main()



#*********************************

def main():
    start_screen()

    points = 20

    inventory = {'torch':1}
    chest_1 = ['key_1', 'shovel', 'torch', 'goldcoin']
    chest_2 = ['key_2', 'torch', 'helmet']
    chest_3 = ['key_3', 'calculator', 'shovel']
    chest_4 = ['key_4', 'calculator', 'torch']
    chest_5 = ['goldcoin','goldcoin','goldcoin','goldcoin','goldcoin','goldcoin','goldcoin',]
    y_axis = 1
    x_axis = 1

    filename = "board_1.csv"

    board = create_board(filename)
    insert_player(board, y_axis, x_axis)


    while True:
        os.system('clear')
        print_board(board)

        print('')
        print("***** Points: ", points,"*****")
        print('')
        print_table(inventory, 1)

        if points < 1:
            print('dupa')
            lose_game()

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

         #0twieranie 1 skrzynki
        if pressedkey == 'o' and filename == 'board_1.csv':
            if board[1][8] == '@' or board[2][9] == '@' or board[2][10] == '@' or board[1][11] == '@':
                if len(chest_1) > 0:
                    print("You opened the chest and found some items. Now it's in your backpack")
                    add_to_inventory(inventory, chest_1)
                    del chest_1[:]
                    time.sleep(2)
                else:
                    print("                     EMPTY")
                    time.sleep(0.5)
            #otwieranie 2 skrzynki
        if pressedkey == 'o' and filename == 'board_2.csv':
            if board[6][23] == '@' or board[5][24] == '@' or board[5][25] == '@':
                if len(chest_2) > 0:
                    print("You opened the chest and found some items. Now it's in your backpack")
                    add_to_inventory(inventory, chest_2)
                    del chest_2[:]
                    time.sleep(2)
                else:
                    print("                     EMPTY")
                    time.sleep(0.5)
            #otwieranie 3 skrzynki
        if pressedkey == 'o' and filename == 'board_3.csv':
            if board[32][35] == '@' or board[33][36] == '@' or board[33][37] == '@':
                if len(chest_3) > 0:
                    print("You opened the chest and found some items. Now it's in your backpack")
                    add_to_inventory(inventory, chest_3)
                    del chest_3[:]
                    time.sleep(2)
                else:
                    print("                     EMPTY")
                    time.sleep(0.5)
            #otwieranie 4 skrzynki
        if pressedkey == 'o' and filename == 'board_4.csv':
            if board[34][6] == '@' or board[35][4] == '@' or board[35][5] == '@':
                if len(chest_4) > 0:
                    print("You opened the chest and found some items. Now it's in your backpack")
                    add_to_inventory(inventory, chest_4)
                    del chest_4[:]
                    time.sleep(2)
                else:
                    print("                     EMPTY")
                    time.sleep(0.5)
            #otwieranie 5 skrzynki
            elif board[30][15] == '@' or board[30][16] == '@':
                if len(chest_5) > 0:
                    print("You opened the chest and found some items. Now it's in your backpack")
                    add_to_inventory(inventory, chest_5)
                    del chest_5[:]
                    time.sleep(2)
                else:
                    print("                     EMPTY")
                    time.sleep(0.5)

#******************************OTWIERANIE DRZWI*********************************
            #otwieranie drzwi na 1 mapie
        if pressedkey == 'o'and filename == 'board_1.csv':
            if board[13][16] =='@' and 'key_1' in inventory :
                board[13][17] = '.'
                del inventory['key_1']
            #otwieranie drzwi na 2 mape z korytarza
        if pressedkey == 'o'and filename == 'board_2.csv':
            if board[11][26] =='@':
                board[11][27] = '.'
            #otwieranie drzwi na 2 mapie
            elif board[13][33] =='@' and 'key_2' in inventory :
                board[14][33] = '.'
                del inventory['key_2']
            #otwieranie drzwi na 3 mape z korytarza
        if pressedkey == 'o'and filename == 'board_3.csv':
            if board[22][35] =='@':
                board[23][35] = '.'
            #otwieranie drzwi na 3 mapie
            elif board[36][27] =='@' and 'key_3' in inventory :
                board[36][26] = '.'
                del inventory['key_3']
            #otwieranie drzwi na 4 mape z korytarza
        if pressedkey == 'o'and filename == 'board_4.csv':
            if board[34][18] =='@':
                board[34][17] = '.'

#***********WŁĄCZANIE MINIGIER**************************************
        if pressedkey == 'g':
            if board[10][3] == '@' or board[11][1] == '@' or board[11][2] == '@':
                first_game()
        if pressedkey == 'g' and filename == 'board_2.csv':
            if board[13][35] == '@' or board[12][36] == '@' or board[12][37] == '@':
                second_game()
        if pressedkey == 'g' and filename == 'board_3.csv':
            if board[25][24] == '@' or board[25][25] == '@' or board[24][26] == '@':
                third_game()
        if pressedkey == 'g' and filename == 'board_4.csv':
            if board[24][1] == '@' or board[25][2] == '@' or board[25][3] == '@':
                os.system('clear')
                guards_main(inventory, board)

#*********************ZMIANA MAPY**************************************

        if board[13][20] == '@':
            filename = "board_2.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)

        if filename =="board_2.csv" and board[16][33] == '@':
            filename = "board_3.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)

        if filename =="board_3.csv" and board[36][24] == '@':
            filename = "board_4.csv"
            board = create_board(filename)
            insert_player(board, y_axis, x_axis)


if __name__ == '__main__':
    main()
