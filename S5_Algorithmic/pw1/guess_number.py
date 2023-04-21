from random import randint

from average import average
from util import type_integer


def play() -> None:
    i = 1
    n = randint(0,100)
    found = False
    while not found:
        print("Find the number between 0 and 100")
        r = type_integer()
        if r == n:
            print(f'Congrats, you found the number in {i} tries!')
            found = True
        elif r < n:
            print('It\'s more')
            i += 1
        else:
            print('It\'s less')
            i += 1


def guess() -> None:
    print('Pick a number between 1 and 100 and write it down (but don\'t tell me :p )')
    r = type_integer()
    found = False
    i = 1
    min, max = 1, 100
    while not found:
        x = int((min + max)/2)
        print(f'Is the answer {x} ?')
        print('Type + if it\'s more, type - if it\'s less, type C if it\'s correct :)')
        s = input()
        if s == '+':
            min = x
        elif s == '-':
            max = x
        elif s == 'C':
            print(f'I found the correct answer in {i} tries !')
            found = True
        else:
            print('Unexpected output detected, stopping the game :(')
            found = True
        i += 1


if __name__ == '__main__':
    guess()