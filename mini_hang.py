import time
import sys
import random
import os

# list of hangman elements ;-)
arts = ["-----\n|   |\n|\n|\n|\n|\n|\n|\n|\n--------",
        "-----\n|   |\n|   0\n|\n|\n|\n|\n|\n|\n--------",
        "-----\n|   |\n|   0\n|  -+-\n|\n|\n|\n|\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\n|\n|\n|\n|\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\ \n|   |\n|\n|\n|\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|\n|\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |\n|\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |\n|  |\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  | |\n|  |\n|\n--------",
        "-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  | |\n|  | |\n|\n--------"]


def get_capital():

    """choose random capital from list"""
    capitals = ('VIENNA', 'BRUSSELS', 'SOFIA', 'ZAGREB', 'NICOSIA', 'PRAQUE', 'COPENHAGEN', 'TALLINN', 'HELSINKI', 'PARIS', 'BERLIN', 'ATHENS', 'BUDAPEST', 'DUBLIN', 'ROME', 'RIGA', 'VILNIUS', 'LUXEMBOURG', 'SKOPJE', 'VALETTA', 'AMSTERDAM', 'WARSAW', 'LISBON', 'BUCHAREST', 'BRATISLAVA', 'LJUBLJANA', 'MADRID', 'STOCKHOLM', 'LONDON')
    return random.choice(capitals).upper()


def replace_dashes_with_letters(capital, guessed, letter):

    """for chosen capital replace dashes with correctly geussed letters"""
    out = ""
    for letter in capital:
        if letter in guessed:
            out = out + letter
        else:
            out = out + " '_' "
    return out


def clear_n_print_arts(lifes):

    """clear screen and print hangman arts"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(arts[9-lifes])


def hang_main():
    os.system('clear')
    # lista sprawdza czy już wygrałeś

    while True:

        capital = get_capital()
        guessed = []    # list of right letters already guessed
        wrong = []      # list of wrong letters already guessed

        # start lifes and timer
        lifes = 10
        print('"_"' * len(capital), "\n You have", lifes, "lifes left")
        start_time = time.time()

        while lifes > 0:

            guess = input("\nGuess a letter at name of capital or full name:").upper()

            if guess == capital:
                out = guess
                print(out)
                break
            dashed_capital = replace_dashes_with_letters(capital, guessed, guess)
            if guess in guessed:
                print("\nAlready guessed", guess)
            elif guess in wrong:
                print("\nAlready guessed", wrong)
                lifes = lifes - 1
                clear_n_print_arts(lifes)
                print("\nWrong letters you\'ve already used:", wrong)
                print("\nYou\'ve already used this wrong letters:", wrong)
            elif guess in capital:
                guessed.append(guess)
                dashed_capital = replace_dashes_with_letters(capital, guessed, guess)
                print(dashed_capital)
                if dashed_capital == capital:
                    print(lifes, "chances left")
                    break

            else:
                print("\nNo")
                lifes = lifes - 1
                clear_n_print_arts(lifes)
                wrong.append(guess)
                print("\nWrong letters you\'ve already used:", wrong)

        if lifes:
            end_time = time.time() - start_time
            print("\nYou guessed ", capital, " it took you {} seconds to guess the number and you have {} lifes left "
                  .format(round(end_time), lifes))
            time.sleep(1.5)
            # zgadłeś, coś dostajesz,może klucz czy coś?
            return

        else:
            print("\nYou didn't get ", capital, "try again!")
            time.sleep(1.5)
            return

if __name__ == '__main__':
    hang_main()
