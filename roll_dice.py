import random
import sys
import time
import csv
import os

min = 1
max = 6
print("To win the game your numbers sum must be equal 7 or 10 or 12. Good luck!")


def dice_main():
    os.system('clear')

    print("Rolling the dices...")
    print("The values are....")
    num_1 = (random.randint(min, max))
    num_2 = (random.randint(min, max))
    print(num_1)
    print(num_2)
    sum = num_1 + num_2
    if sum == 7 or sum == 10 or sum == 12:
        print("You win!")
        time.sleep(2)
        print('You earned: ', sum, "points")

        points_roll = [sum]

        with open('points.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(points_roll)
        return
    else:
        play_again()


def play_again():
    decision = input("Press 'y' to roll again or any other key to escape the program:  ").lower()
    if decision == "y":
        dice_main()
    else:
        return

if __name__ == '__main__':
    dice_main()
