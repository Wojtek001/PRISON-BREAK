import random
import csv
import os


riddles = {'I go in hard. I come out soft. You blow me hard. What am I?': 'chewing gum',
           'What belongs to you but others use it more than you do?': 'name',
           'I’m not an air plane, but I fly through the sky. I’m not a river, but I’m full of water. What am I?': 'cloud',
           'What body part is pronounced as one letter but written with three, only two different letters are used?': 'eye'}


def riddle():
    os.system('clear')
    points_riddle = 0
    for key in riddles:
        print(key)
        answer = input()
        if answer.lower() == riddles[key]:
            points_riddle += 10
            print(points_riddle)
            print('Good answer, congrats!')
        else:
            print('Wrong!')

    points_riddle = [points_riddle]

    with open('points.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(points_riddle)

    print("sum: ",points_riddle)



if __name__ == '__main__':
    riddle()
