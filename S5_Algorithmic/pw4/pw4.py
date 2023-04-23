from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterator


# Exo 1


@dataclass
class LinkedList:
    size: int
    sentinelle: Cell


@dataclass
class Cell:
    value: int
    next: Cell
    prev: Cell


def ll_new() -> LinkedList:
    sent = Cell(None, None, None)
    sent.next = sent
    sent.prev = sent
    return LinkedList(0, sent)


def ll_is_empty(l: LinkedList) -> bool:
    return l.size == 0


def ll_len(l: LinkedList) -> int:
    return l.size


def ll_head(l: LinkedList) -> Optional[Cell]:
    if l.size == 0:
        return None
    return l.sentinelle.next


def ll_tail(l: LinkedList) -> Optional[Cell]:
    if l.size == 0:
        return None
    return l.sentinelle.prev


def ll_str(l: LinkedList) -> str:
    s = ""
    c = l.sentinelle
    for i in range(l.size):
        c = c.next
        s += str(c.value) + "⥂"
    return s[:-1]


# Exo 2
def ll_lookup(l: LinkedList, item: int) -> Optional[Cell]:
    c = l.sentinelle
    for i in range(l.size):
        c = c.next
        if c.value == item:
            return c
    return None


def ll_cell_at(l: LinkedList, i: int) -> Cell:
    if i >= l.size:
        raise IndexError("Index is too big")
    c = l.sentinelle
    for j in range(i + 1):
        c = c.next
    return c


def ll_get(l: LinkedList, idx: Cell) -> int:
    c = l.sentinelle
    while c.next != idx:
        c = c.next
        if c == l.sentinelle:
            raise IndexError("Cell not in the list")
    return c.next.value


def ll_set(l: LinkedList, idx: Cell, item: int) -> LinkedList:
    c = l.sentinelle
    while c.next != idx:
        c = c.next
        if c == l.sentinelle:
            raise IndexError("Cell not in the list")
    c.next.value = item
    return l


def ll_insert(
    l: LinkedList, item: int, neighbor: Cell, after: bool = True
) -> LinkedList:
    c = l.sentinelle
    while c.next != neighbor:
        c = c.next
        if c == l.sentinelle:
            raise IndexError("Cell not in the list")
    # Arrived to the cell before the neighbor
    if not after:
        new = Cell(item, neighbor, c)
        c.next = new
        new.next.prev = new
    else:
        c = c.next.next  # Go to the cell after the neighbor
        new = Cell(item, c, neighbor)
        c.prev = new
        new.prev.next = new
    l.size += 1
    return l


def ll_append(l: LinkedList, item: int) -> LinkedList:
    return ll_insert(l, item, l.sentinelle.prev)


def ll_prepend(l: LinkedList, item: int) -> LinkedList:
    return ll_insert(l, item, l.sentinelle.next, False)


def ll_remove(l: LinkedList, cell: Cell) -> LinkedList:
    c = l.sentinelle
    while c.next != cell:
        c = c.next
        if c == l.sentinelle:
            raise IndexError("Cell not in the list")
    c.next = c.next.next
    c.next.prev = c
    l.size -= 1
    return l


def ll_extend(l1: LinkedList, l2: LinkedList) -> LinkedList:
    c = ll_tail(l1)  # Take last cell of l1
    c.next = ll_head(l2)  # Its last cell is the first of l2
    ll_head(
        l2
    ).prev = c  # The previous value of the first cell of l2 is now the last of l1

    ll_tail(
        l2
    ).next = (
        l1.sentinelle
    )  # # The next value of the last cell of l2 is now the sentinel of l1
    l1.sentinelle.prev = ll_tail(
        l2
    )  # The previous value of the sentinel of l1 is now the last cell of l2
    l1.size += l2.size  # Change the size and it's all good :)
    return l1


# Exo 3


def ll_reverse(l: LinkedList, k: int) -> LinkedList:
    if k > ll_len(l) or k <= 0:
        raise IndexError("Index error")

    for i in range(k // 2):
        ll_swap(l, i, k - i - 1)
    return l


def ll_swap(l: LinkedList, i: int, j: int) -> LinkedList:
    if i > j:
        return ll_swap(l, j, i)

    before_c1 = ll_cell_at(l, i - 1)
    after_c1 = ll_cell_at(l, i + 1)

    before_c2 = ll_cell_at(l, j - 1)
    try:
        after_c2 = ll_cell_at(l, j + 1)
    except IndexError:
        after_c2 = ll_head(l)

    c1 = ll_cell_at(l, i)
    c2 = ll_cell_at(l, j)

    if i + 1 != j:  # Si i et j ne sont pas côte à côte
        c1.next, c1.prev, c2.next, c2.prev = c2.next, c2.prev, c1.next, c1.prev

        before_c1.next = c2
        after_c1.prev = c2

        before_c2.next = c1
        after_c2.prev = c1

    else:
        c1.next, c1.prev, c2.next, c2.prev = c2.next, c2, c1, c1.prev

        before_c1.next = c2

        after_c2.prev = c1

    return l


def permutations(l: LinkedList) -> Iterator[LinkedList]:
    if ll_len(l) == 1:
        yield l
    elif ll_len(l) == 2:
        yield l
        yield ll_reverse(l, 2)
    else:
        for i in range(ll_len(l)):
            v = ll_cell_at(l, i).value
            l = ll_remove(l, ll_cell_at(l, i))
            j = 0
            for p in permutations(l):
                yield ll_insert(l, v, ll_cell_at(l, j))
                ll_remove(l, ll_cell_at(l, j + 1))
            ll_insert(l, v, ll_cell_at(l, i - 1), False)


def topswops(n: int) -> int:
    l = ll_new()
    for i in range(1, n + 1):
        ll_append(l, i)
    max = 0
    for p in permutations(l):
        c = 0
        v = ll_head(p).value
        while v != 1:
            p = ll_reverse(p, v)
            c += 1
            v = ll_head(p).value
        if c > max:
            max = c
    return max


# I give up, permutations and/or topswops don't work


def merge_sort(l: list) -> list:
    if len(l) > 1:
        m = len(l) // 2
        left = l[:m]
        right = l[m:]

        left = merge_sort(left)
        right = merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    return l


@dataclass
class Deque:
    l: LinkedList


def d_new() -> Deque:
    return Deque(ll_new())


def d_is_empty(d: Deque) -> bool:
    return ll_is_empty(d.l)


def d_len(d: Deque) -> int:
    return ll_len(d.l)


def d_str(d: Deque) -> str:
    s = "["
    for i in range(d_len(d)):
        s += str(ll_get(d.l, ll_cell_at(d.l, i))) + ","
    s = s[:-1]
    s += "]"
    return s


def d_front(d: Deque) -> int:
    return ll_get(d.l, ll_head(d.l))


def d_queue(d: Deque) -> int:
    return ll_get(d.l, ll_tail(d.l))


def d_push_front(d: Deque, item: int) -> Deque:
    d.l = ll_prepend(d.l, item)
    return d


def d_push_rear(d: Deque, item: int) -> Deque:
    d.l = ll_append(d.l, item)
    return d


def d_pop_front(d: Deque) -> Deque:
    d.l = ll_remove(d.l, ll_head(d.l))
    return d


def d_pop_rear(d: Deque) -> Deque:
    d.l = ll_remove(d.l, ll_tail(d.l))
    return d


def simple_max_value(l: list[int], k: int) -> None:
    for i in range(len(l) - k + 1):
        sub = l[i : i + k]
        print(f"Maximum of {sub} = {max(sub)}")


def deque_max_value(l: list[int], k: int) -> None:
    d = d_new()
    for i in range(k):
        if d_is_empty(d):
            d_push_front(d, l[i])
        while not d_is_empty(d) and d_queue(d) < l[i]:
            d_pop_rear(d)
        d_push_rear(d, l[i])
    for i in range(k, len(l)):
        print(f"Max de {l[i - k:i]} = {d_front(d)}")
        if d_front(d) not in l[i - k : i]:
            d_pop_front(d)
        while not d_is_empty(d) and d_queue(d) < l[i]:
            d_pop_rear(d)
        d_push_rear(d, l[i])
