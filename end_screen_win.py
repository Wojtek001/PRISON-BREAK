import time
import sys


def end_screen():
    for i in range(20):
        print("")
    print('''
         /$$     /$$                                                               /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$$       /$$ /$$
        |  $$   /$$/                                                              | $$_____/| $$__  $$| $$_____/| $$_____/      | $$| $$
         \  $$ /$$/   /$$$$$$  /$$   /$$        /$$$$$$   /$$$$$$   /$$$$$$       | $$      | $$  \ $$| $$      | $$            | $$| $$
          \  $$$$/   /$$__  $$| $$  | $$       |____  $$ /$$__  $$ /$$__  $$      | $$$$$   | $$$$$$$/| $$$$$   | $$$$$         | $$| $$
           \  $$/   | $$  \ $$| $$  | $$        /$$$$$$$| $$  \__/| $$$$$$$$      | $$__/   | $$__  $$| $$__/   | $$__/         |__/|__/
            | $$    | $$  | $$| $$  | $$       /$$__  $$| $$      | $$_____/      | $$      | $$  \ $$| $$      | $$                    
            | $$    |  $$$$$$/|  $$$$$$/      |  $$$$$$$| $$      |  $$$$$$$      | $$      | $$  | $$| $$$$$$$$| $$$$$$$$       /$$ /$$
            |__/     \______/  \______/        \_______/|__/       \_______/      |__/      |__/  |__/|________/|________/      |__/|__/

                                                                                                                               ''')
    for i in range(20):
        print("")
    
    time.sleep(2)
    sys.exit()


if __name__ == '__main__':
    end_screen()

    
