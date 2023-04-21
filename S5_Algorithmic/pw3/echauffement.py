from tp1.TP1 import saisir_entier
from random import randint


def saisir_tableau() -> list[int]:
    l = []
    x = saisir_entier()
    while x is not None:
        l.append(x)
        x = saisir_entier()
    return l


def remplir_tableau(n: int, a: int = 0, b: int = 100) -> list[int]:
    return [randint(a, b) for i in range(n)]



def inverser_tableau(l: list = None) -> list:
    if l is None:
        l = saisir_tableau()
    length = len(l)
    ll = [0] * length
    for i in range(length-1, -1,-1):
        ll[length-i-1] = l[i]
    return ll


def palindrome() -> None:
    s = input("Type a word\n")
    while s != '':
        if s == ''.join(inverser_tableau(s)):
            print("Palindrome YEP")
        else:
            print("Palindrome NOPE")
        s = input("Type another word\n")


def order_odd_and_even(l: list[int]) -> list[int]:
    length = len(l)
    ll = [0] * length
    min, max = 0, length-1
    for i in range(length):
        if l[i]%2 == 0:
            ll[min] = l[i]
            min += 1
        else:
            ll[max] = l[i]
            max -= 1
    return ll


def order_odd_and_even_improved(l: list[int]) -> list[int]:
    length = len(l)
    c = 0
    for i in range(length//2):
        while l[i]%2 == 1:
            l[i], l[length-1-c] = l[length-1-c], l[i]
            c += 1
    return l



if __name__ == '__main__':
    pass