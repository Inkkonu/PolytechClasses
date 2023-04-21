from __future__ import annotations


class Node:

    def __init__(self, value: int, parent: Node, left: Node, right: Node):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def equal(self, other: Node, sentinelle: Node, other_sentinelle: Node) -> bool:
        if self is sentinelle and other is other_sentinelle:
            return True
        if self.value != other.value:
            return False
        return self.left.equal(other.left, sentinelle, other_sentinelle) and self.right.equal(other.right, sentinelle,
                                                                                              other_sentinelle)
