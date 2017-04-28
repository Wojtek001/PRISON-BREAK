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




    You are a prisoner in Fort Knox.
    They caught you when you stole a loaf of bread and sentenced you for 20 years because you are black.
    You disagree with this unjust punishment, and the only thing you think about is to escape from here.
    From your fellow prisoners you hearded about the legendary map of tunnels unnder the prison,
    that will allow you to get out of here.
    To run out from here you will have to find all 4 pieces of legandary map which helps you avoid all traps
    hidden in floor and walls.
    Your task is to get out from the prison and escape from (or kill) all the guards!




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
