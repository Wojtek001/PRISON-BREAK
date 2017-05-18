import sys


def end_screen():
    for i in range(20):
        print("")
    print('''
                 /$$     /$$                           /$$        /$$$$$$   /$$$$$$  /$$$$$$$$       /$$ /$$
                |  $$   /$$/                          | $$       /$$__  $$ /$$__  $$| $$_____/      | $$| $$
                 \  $$ /$$/   /$$$$$$  /$$   /$$      | $$      | $$  \ $$| $$  \__/| $$            | $$| $$
                  \  $$$$/   /$$__  $$| $$  | $$      | $$      | $$  | $$|  $$$$$$ | $$$$$         | $$| $$
                   \  $$/   | $$  \ $$| $$  | $$      | $$      | $$  | $$ \____  $$| $$__/         |__/|__/
                    | $$    | $$  | $$| $$  | $$      | $$      | $$  | $$ /$$  \ $$| $$
                    | $$    |  $$$$$$/|  $$$$$$/      | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$       /$$ /$$
                    |__/     \______/  \______/       |________/ \______/  \______/ |________/      |__/|__/
                                                                                                                               ''')
    for i in range(20):
        print("")

    quit = input("To quit press q, to play again press any key").lower()
    if quit == q:
        sys.exit()




if __name__ == '__main__':
    end_screen()
