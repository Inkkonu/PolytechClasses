from __future__ import annotations

class Cell:

    def __init__(self, value: int, next: Cell, prev: Cell):
        self.value = value
        self.next = next
        self.prev = prev