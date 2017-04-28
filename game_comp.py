import os
import time

def welcome():
    os.system('clear')
    for i in range(20):
        print("")
    print('''                       /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$  /$$   /$$       /$$$$$$$  /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$   /$$
                      | $$__  $$| $$__  $$|_  $$_/ /$$__  $$ /$$__  $$| $$$ | $$      | $$__  $$| $$__  $$| $$_____/ /$$__  $$| $$  /$$/
                      | $$  \ $$| $$  \ $$  | $$  | $$  \__/| $$  \ $$| $$$$| $$      | $$  \ $$| $$  \ $$| $$      | $$  \ $$| $$ /$$/
                      | $$$$$$$/| $$$$$$$/  | $$  |  $$$$$$ | $$  | $$| $$ $$ $$      | $$$$$$$ | $$$$$$$/| $$$$$   | $$$$$$$$| $$$$$/
                      | $$____/ | $$__  $$  | $$   \____  $$| $$  | $$| $$  $$$$      | $$__  $$| $$__  $$| $$__/   | $$__  $$| $$  $$
                      | $$      | $$  \ $$  | $$   /$$  \ $$| $$  | $$| $$\  $$$      | $$  \ $$| $$  \ $$| $$      | $$  | $$| $$\  $$
                      | $$      | $$  | $$ /$$$$$$|  $$$$$$/|  $$$$$$/| $$ \  $$      | $$$$$$$/| $$  | $$| $$$$$$$$| $$  | $$| $$ \  $$
                      |__/      |__/  |__/|______/ \______/  \______/ |__/  \__/      |_______/ |__/  |__/|________/|__/  |__/|__/  \__/''')

    for i in range(20):
        print("")
    time.sleep(3)


def intro_screen():
    os.system('clear')
    for i in range(20):
        print("")
    print('''
                                You are a prisoner in Fort Knox. Your task is to get out from the prison and kill all the guards!
                                To run out you will have to find all 4 pieces of map which help you to avoid all traps hidden
                                in floor and walls. GL & HF
    ''')


    print('''
                                                    Controls:
                                                    w - move up             o - open (chests/ dors)
                                                    s - move down           u - use items
                                                    a - move left           q - quit game
                                                    d - move right
    ''')


    for i in range(20):
        print("")

welcome()
intro_screen()
