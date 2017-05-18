import random
import game_my1_3

riddles = {'I go in hard. I come out soft. You blow me hard. What am I?': 'chewing gum',
           'What belongs to you but others use it more than you do?': 'name',
           'I’m not an air plane, but I fly through the sky. I’m not a river, but I’m full of water. What am I?': 'cloud',
           'What body part is pronounced as one letter but written with three, only two different letters are used?': 'eye'}


def riddle():

    for key in riddles:
        points = 0
        print(key)
        answer = input()
        if answer.lower() == riddles[key]:
            points += 1
            print('Good answer, congrats!')
        
        else:
            print('Wrong!')
    


if __name__ == '__main__':
    riddle()