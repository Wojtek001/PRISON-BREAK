import random

number_to_guess = str(random.randint(100,1000))
# print(number_to_guess)

def user_guess():
    number_to_guess = str(random.randint(100,1000))
    print(number_to_guess)
    while True:
        user_guess = input("Type a 3 digit number: ")
        guess_number = []
        for digit in number_to_guess:
            guess_number.append(digit)


        user_number = []
        for digit in user_guess:
            user_number.append(digit)
        print(user_number)

        clues_list = []

        for i in range(3):
            if user_number[i] == guess_number[i]:
                clues_list.insert(0,"Hot")
            elif user_number[i] != guess_number[i] and user_number[i] in guess_number :
                clues_list.append("Warm")
        print(*clues_list)

        if not any(digit in guess_number for digit in user_number):
                print('cold')

        if clues_list == ['Hot','Hot','Hot']:
            return






if __name__ == '__main__':
    user_guess()
