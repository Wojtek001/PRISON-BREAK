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
            ....
            ....
            ....
    ''')

    for i in range(20):
        print("")

welcome()
intro_screen()