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

    Your task is to get out from the prison and avoid traps hidden in the floor!




    ''')

    print('''
                                                    Controls:

                                                    w - move up             o - open (chests/ dors)
                                                    s - move down           g - play mini game
                                                    a - move left           q - quit game
                                                    d - move right

    ''')


    for i in range(15):
        print("")
    go_back = input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRESS ANY KEY TO CONTINUE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>").lower()
    for i in range(5):
        print("")
    if go_back == "c":
        return
    else:
        None
def main():
    welcome()
    intro_screen()



if __name__ == '__main__':
    main()
