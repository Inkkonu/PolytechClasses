from __future__ import annotations
from cell import Cell


class LinkedList:
    def __init__(self):
        sentinel = Cell(None, None, None)
        sentinel.next = sentinel
        sentinel.prev = sentinel
        self.size = 0
        self.sentinel = sentinel

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def head(self):
        if self.is_empty():
            return None
        return self.sentinel.next

    def tail(self):
        if self.is_empty():
            return None
        return self.sentinel.prev

    def __str__(self):
        s = ""
        c = self.sentinel
        for i in range(len(self)):
            c = c.next
            s += str(c.value) + "⥂"
        return s[:-1]

    def lookup(self, item: int):
        c = self.sentinel
        for i in range(len(self)):
            c = c.next
            if c.value == item:
                return c
        return None

    def cell_at(self, index: int):
        if index >= len(self):
            raise IndexError("Error, index is too big")
        c = self.sentinel
        for i in range(index + 1):
            c = c.next
        return c

    def get(self, idx: Cell):
        c = self.sentinel
        while c.next != idx:
            c = c.next
            if c == self.sentinel:
                raise IndexError("Cell not in the list")
        return c.next.value

    def set(self, idx: Cell, item: int):
        c = self.sentinel
        while c.next != idx:
            c = c.next
            if c == self.sentinel:
                raise IndexError("Cell not in the list")
        c.next.value = item
        return self

    def insert(self, item: int, neighbor: Cell, after: bool = True):
        c = self.sentinel
        while c.next != neighbor:
            c = c.next
            if c == self.sentinel:
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
        self.size += 1
        return self

    def append(self, item: int):
        return self.insert(item, self.sentinel.prev)

    def prepend(self, item: int):
        return self.insert(item, self.sentinel.next, False)

    def remove(self, cell: Cell):
        c = self.sentinel
        while c.next != cell:
            c = c.next
            if c == self.sentinel:
                raise IndexError("Cell not in the list")
        c.next = c.next.next
        c.next.prev = c
        self.size -= 1
        return self

    def extend(self, l: LinkedList):
        if not l.is_empty():
            if self.is_empty():
                self = l
            else:
                c = self.tail()  # Take last cell of l1
                c.next = l.head()  # Its last cell is the first of l2
                l.head().prev = c  # The previous value of the first cell of l2 is now the last of l1

                l.tail().next = (
                    self.sentinel
                )  # The next value of the last cell of l2 is now the sentinel of l1
                self.sentinel.prev = (
                    l.tail()
                )  # The previous value of the sentinel of l1 is now the last cell of l2
                self.size += len(l)  # Change the size and it's all good :)
        return self

    def reverse(self, k: int):
        if k > len(self) or k <= 0:
            raise IndexError("Index error")

        for i in range(k // 2):
            self.swap(i, k - i - 1)
        return self

    def swap(self, i: int, j: int):
        if i > j:
            return self.swap(j, i)

        before_c1 = self.cell_at(i - 1)
        after_c1 = self.cell_at(i + 1)

        before_c2 = self.cell_at(j - 1)
        try:
            after_c2 = self.cell_at(j + 1)
        except IndexError:
            after_c2 = self.head()

        c1 = self.cell_at(i)
        c2 = self.cell_at(j)

        if i + 1 != j:  # If i and j are not consecutive
            c1.next, c1.prev, c2.next, c2.prev = c2.next, c2.prev, c1.next, c1.prev

            before_c1.next = c2
            after_c1.prev = c2

            before_c2.next = c1
            after_c2.prev = c1

        else:
            c1.next, c1.prev, c2.next, c2.prev = c2.next, c2, c1, c1.prev

            before_c1.next = c2

            after_c2.prev = c1

        return self


if __name__ == "__main__":
    l = LinkedList()
    l.append(4)
    l.append(5)
    l.prepend(1)
    print(l)
    l = l.reverse(3)
    print(l)
