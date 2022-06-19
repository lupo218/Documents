from random import randint
from os import system
def get_guess_from_user(x):
    print('Please guess a number:')
    choose = int(input())
    system('cls')
    if generate_number(choose) == x:
        return f"I also chose:{x} well done !!!"
    else:
        return f"I chose:{x} you did not succeed ... too bad"

def generate_number(n):
    result = randint(1,n)
    return result