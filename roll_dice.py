import random
import sys
min = 1
max = 6
print("To win the game your numbers sum must be equal 7 or 10 or 12. Good luck!")


def dice_main():

    print("Rolling the dices...")
    print("The values are....")
    num_1 = (random.randint(min, max))
    num_2 = (random.randint(min, max))
    print(num_1)
    print(num_2)
    sum = num_1 + num_2
    if sum == 7 or sum == 10 or sum == 12:
        print("You win!")
        sys.exit()
    else:
        play_again()


def play_again():
    decision = input("Press 'y' to roll again or any other key to escape the program:  ").lower()
    if decision == "y":
        main()
    else:
        print('See You later!')
        sys.exit()


dice_main()
