from random import randint

from tp1.moyenne import moyenne
from tp1.util import saisir_entier


def jouer() -> None:
    i = 1
    n = randint(0,100)
    found = False
    while not found:
        print("Trouve le nombre entre 0 et 100")
        r = saisir_entier()
        if r == n:
            print(f'Bravo, vous avez trouvé le résultat en {i} essais!')
            found = True
        elif r < n:
            print('C\'est plus!')
            i += 1
        else:
            print('C\'est moins!')
            i += 1


def guess() -> None:
    print('Pick a number between 1 and 100 and write it down (but don\'t tell me :p )')
    r = saisir_entier()
    found = False
    i = 1
    min, max = 1, 100
    while not found:
        x = int(moyenne(min, max))
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