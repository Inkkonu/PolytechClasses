import time
from tp3.TP3 import remplir_tableau


def selection_tri(l: list) -> list:
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1, len(l)):
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

if __name__ == '__main__':
    for i in [100, 1_000, 10_000, 100_000, 1_000_000]:
        l = remplir_tableau(i)

        start = time.perf_counter()
        bubble_tri(l)
        end = time.perf_counter()
        print(end - start)