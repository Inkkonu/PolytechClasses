from __future__ import annotations
from donnees import *


class Cell:

    def __init__(self, value, next: Cell, prev: Cell):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:

    def __init__(self):
        sentinelle = Cell(None, None, None)
        sentinelle.next = sentinelle
        sentinelle.prev = sentinelle
        self.size = 0
        self.sentinelle = sentinelle

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def head(self):
        if self.is_empty():
            return None
        return self.sentinelle.next

    def tail(self):
        if self.is_empty():
            return None
        return self.sentinelle.prev

    def __str__(self):
        s = ''
        c = self.sentinelle
        for i in range(len(self)):
            c = c.next
            s += str(c.value) + '⥂'
        return s[:-1]

    def lookup(self, item):
        c = self.sentinelle
        for i in range(len(self)):
            c = c.next
            if c.value == item:
                return c
        return None

    def cell_at(self, index: int):
        if index >= len(self):
            raise IndexError('Error, index is too big')
        c = self.sentinelle
        for i in range(index + 1):
            c = c.next
        return c

    def get(self, idx: Cell):
        c = self.sentinelle
        while c.next != idx:
            c = c.next
            if c == self.sentinelle:
                raise IndexError('Cell not in the list')
        return c.next.value

    def set(self, idx: Cell, item):
        c = self.sentinelle
        while c.next != idx:
            c = c.next
            if c == self.sentinelle:
                raise IndexError('Cell not in the list')
        c.next.value = item
        return self

    def insert(self, item, neighbor: Cell, after: bool = True):
        c = self.sentinelle
        while c.next != neighbor:
            c = c.next
            if c == self.sentinelle:
                raise IndexError('Cell not in the list')
        # On est arrivé à la case juste avant le neighbor
        if not after:
            new = Cell(item, neighbor, c)
            c.next = new
            new.next.prev = new
        else:
            c = c.next.next  # On va à la case juste après le neighbor
            new = Cell(item, c, neighbor)
            c.prev = new
            new.prev.next = new
        self.size += 1
        return self

    def append(self, item):
        return self.insert(item, self.sentinelle.prev)

    def prepend(self, item):
        return self.insert(item, self.sentinelle.next, False)

    def remove(self, cell: Cell):
        c = self.sentinelle
        while c.next != cell:
            c = c.next
            if c == self.sentinelle:
                raise IndexError('Cell not in the list')
        c.next = c.next.next
        c.next.prev = c
        self.size -= 1
        return self


def question_1_1_1(ligne):
    ll = LinkedList()
    for arret in ligne:
        ll.append(arret)
    return ll


def question_1_1_2():
    ll = question_1_1_1(ligne1)
    ll.insert("Bouffay", ll.lookup("Commerce"))
    return ll


def question_1_1_3():
    ll = question_1_1_1(ligne1)
    ll.remove(ll.lookup("Croix-Bonneau"))
    return ll


def question_1_2_1():
    l = []
    for ligne in reseau:
        l.append(question_1_1_1(ligne))
    return l


def question_1_2_2(arret1, arret2):
    r = question_1_2_1()
    i = 0
    for ligne in r:
        if ligne.lookup(arret1) is not None and ligne.lookup(arret2) is not None:
            # Si les deux arrêts sont présents dans la même LinkedList, alors la ligne est directe
            return i
        i += 1


def question_1_2_3(arret):
    r = question_1_2_1()
    i = 0
    l = []
    for ligne in r:
        if ligne.lookup(arret) is not None:
            # Si l'arrêt est dans la LinkedList
            l.append(i)
        i += 1
    return l
