from tp1.TP1 import saisir_entier
from random import randint
from dataclasses import dataclass
from typing import Optional
import ctypes


# Exo 1
def saisir_tableau() -> list[int]:
    l = []
    x = saisir_entier()
    while x is not None:
        l.append(x)
        x = saisir_entier()
    return l


def remplir_tableau(n: int, a: int = 0, b: int = 100) -> list[int]:
    return [randint(a, b) for i in range(n)]


# Exo 2
def inverser_tableau() -> list[int]:
    l = saisir_tableau()
    length = len(l)
    ll = [0] * length
    for i in range(length - 1, -1, -1):
        ll[length - i - 1] = l[i]
    return ll


# Exo 3
def palindrome() -> None:
    s = input("Type a word\n")
    while s != '':
        if s == ''.join(inverser_tableau(s)):
            print("Palindrome YEP")
        else:
            print("Palindrome NOPE")
        s = input("Type another word\n")


# Exo 4
def order_odd_and_even(l: list[int]) -> list[int]:
    length = len(l)
    ll = [0] * length
    min, max = 0, length - 1
    for i in range(length):
        if l[i] % 2 == 0:
            ll[min] = l[i]
            min += 1
        else:
            ll[max] = l[i]
            max -= 1
    return ll


def order_odd_and_even_improved(l: list[int]) -> list[int]:
    length = len(l)
    c = 0
    for i in range(length // 2):
        while l[i] % 2 == 1:
            l[i], l[length - 1 - c] = l[length - 1 - c], l[i]
            c += 1
    return l


# Exo 7
@dataclass
class ArrayList:
    max_size: int
    current_size: int
    array: ctypes.Array


def al_new(m: int = 10, l: list[int] = None) -> ArrayList:
    current = min(len(l), m)
    tab = ArrayList(m, current, None)
    ArrayType = ctypes.c_int * m
    tab.array = ArrayType()
    for i in range(current):
        tab.array[i] = l[i]
        # print(i, tab.array[i])
    return tab


def al_len(tab: ArrayList) -> int:
    return tab.current_size


def al_is_empty(tab: ArrayList) -> bool:
    return tab.current_size == 0


def al_str(tab: ArrayList) -> str:
    s = '['
    for i in range(al_len(tab)):
        s += str(tab.array[i]) + ', '
    s += ']'
    return ''.join(s.rsplit(', ', 1))  # Remove last occurence of ', '


# Exo 8
def al_get(tab: ArrayList, i: int) -> int:
    try:
        return tab.array[i]
    except IndexError:
        print('Index non valide')
        return None


def al_set(tab: ArrayList, i: int, item: int) -> ArrayList:
    try:
        tab.array[i] = item
    except IndexError:
        print('Index non valide')
    return tab


def al_lookup(tab: ArrayList, item: int) -> Optional[int]:
    for i in range(tab.current_size):
        if tab.array[i] == item:
            return i
    return None


def al_remove(tab: ArrayList, i: int) -> ArrayList:
    if i > tab.current_size - 1:
        print('Index non valide')
    else:
        for j in range(i, tab.current_size):
            tab.array[j] = tab.array[j + 1]
        tab.current_size -= 1
    return tab


def al_insert(tab: ArrayList, i: int, item: int) -> ArrayList:
    if tab.current_size == tab.max_size:
        raise OverflowError("Dépassement de capacité")
    for j in range(tab.current_size, i, -1):
        tab.array[j] = tab.array[j - 1]
    tab.array[i] = item
    tab.current_size += 1
    return tab


def al_prepend(tab: ArrayList, item: int) -> ArrayList:
    return al_insert(tab, 0, item)


def al_append(tab: ArrayList, item: int) -> ArrayList:
    return al_insert(tab, tab.current_size, item)


def al_extend(tab1: ArrayList, tab2: ArrayList) -> ArrayList:
    n = min(tab1.max_size - tab1.current_size, al_len(tab2))
    for i in range(n):
        tab1.array[i + tab1.current_size] = tab2.array[i]
    tab1.current_size += n
    return tab1


# Exo 9
def al_doublon(tab: ArrayList) -> ArrayList:
    doublons = []
    for i in range(al_len(tab)):
        j = abs(al_get(tab, i))
        n = al_get(tab, j)
        if n > 0:
            al_set(tab, j, -n)
        else:
            if j not in doublons:
                doublons.append(j)

    for i in range(al_len(tab)):
        al_set(tab, i, abs(al_get(tab, i)))

    return al_new(l=doublons)


# Exo 10
def dicho(tab: ArrayList, n: int, min: int = 0, max: int = 100) -> int:
    if n < 0 or n > 100 or min + 1 == max:
        return -1
    m = (min + max) // 2
    if n == al_get(tab, m):
        return m
    if n < al_get(tab, m):
        return dicho(tab, n, min, m)
    if n > al_get(tab, m):
        return dicho(tab, n, m, max)


def ask_for_dicho() -> None:
    n = saisir_entier()
    while n is not None:
        tab = al_new(100, sorted(remplir_tableau(100)))
        print(al_str(tab))
        i = dicho(tab, n)
        print(f'Index of {n} in the array : {i} (if -1 then it has not been found in the array)\n')
        n = saisir_entier()


# Exo 11
def quicksort(tab: ArrayList, begin: int = 0, end: int = None) -> None:
    if end is None:
        end = al_len(tab) - 1
    if begin >= end:
        return
    pivot = partition(tab, begin, end)
    quicksort(tab, begin, pivot - 1)
    quicksort(tab, pivot + 1, end)


def partition(tab: ArrayList, begin: int, end: int) -> int:
    pivot = begin
    for i in range(begin + 1, end + 1):
        if tab.array[i] <= tab.array[begin]:
            pivot += 1
            tab.array[i], tab.array[pivot] = tab.array[pivot], tab.array[i]
    tab.array[pivot], tab.array[begin] = tab.array[begin], tab.array[pivot]
    return pivot


# Exo 12
@dataclass
class Stack:
    tab: ArrayList


def s_new(n: int = 10) -> Stack:
    s = Stack(al_new(n, None))
    return s


def s_size(s: Stack) -> int:
    return al_len(s.tab)


def s_is_empty(s: Stack) -> bool:
    return al_is_empty(s.tab)


def s_str(s: Stack) -> str:
    st = ''
    for i in range(s_size(s) - 1, -1, -1):
        st += str(al_get(s.tab, i)) + "\n"
    return st


def s_push(s: Stack, item: int) -> Stack:
    al_append(s.tab, item)
    return s


def s_pop(s: Stack) -> Stack:
    if not s_is_empty(s):
        al_remove(s.tab, s_size(s) - 1)
    return s


def s_top(s: Stack) -> Optional[int]:
    if not s_is_empty(s):
        return al_get(s.tab, s_size(s) - 1)


# Exo 13
def npi() -> int:
    p = s_new(100)
    print("Type your expression\n")
    s = input()
    while s != '':
        try:
            s_push(p, int(s))
        except ValueError:
            a = s_top(p)
            p = s_pop(p)
            b = s_top(p)
            p = s_pop(p)
            r = int(eval(str(b) + s + str(a)))
            s_push(p, r)
        s = input()
    return s_top(p)


# Exo 14
# Pas fini et flemme en vrai

# Exo 15
# Je l'ai fait pour les listes mais ça marcherait pareil avec notre dataclass queue
def reverse_queue(l: list) -> list:
    if len(l) == 1:
        return l
    return [l.pop()] + reverse_queue(l)


# Exo 16
def bourreau(l: list, k: int) -> int:
    k -= 1
    i = k
    while len(l) != 1:
        l.pop(i)
        i = (i + k) % len(l)
    return l[0]


# Exo 17
def selection_tri(l: list) -> list:
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j

    l[i], l[min_idx] = l[min_idx], l[i]


def insertion_tri(l):
    for i in range(1, len(l)):

        key = l[i]

        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def bubble_tri(l):
    n = len(l)

    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

# Exo 19
