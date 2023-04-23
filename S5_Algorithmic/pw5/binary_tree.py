from __future__ import annotations
from node import Node
from typing import Optional
from pw4.linked_list import LinkedList


class BinaryTree:
    def __init__(self, nodes: Optional[list[Optional[int]]]):
        self.sentinelle = Node(None, None, None, None)
        self.sentinelle.right = self.sentinelle
        if nodes is not None and nodes != []:
            self.sentinelle.left = self.__build_tree(self.sentinelle, 0, nodes)

    def __build_tree(self, node: Node, i: int, nodes: list[int]) -> Optional[Node]:
        if i >= len(nodes) or nodes == []:
            return self.sentinelle
        n = Node(nodes[i], node, None, None)
        n.left = self.__build_tree(n, 2 * i + 1, nodes)
        n.right = self.__build_tree(n, 2 * i + 2, nodes)
        return n

    def is_empty(self) -> bool:
        return self.root() is None

    def root(self) -> Optional[Node]:
        if self.sentinelle.left is None:
            return self.sentinelle
        return self.sentinelle.left

    def terminal(self) -> Node:
        return self.sentinelle

    def __height(self, node: Node) -> int:
        if node == self.sentinelle:
            return -1
        return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self) -> int:
        return self.__height(self.root())

    def __size(self, node: Node) -> int:
        if node == self.sentinelle:
            return 0
        return 1 + self.__size(node.left) + self.__size(node.right)

    def size(self) -> int:
        return self.__size(self.root())

    def equal(self, other: BinaryTree) -> bool:
        return self.root().equal(other.root(), self.sentinelle, other.sentinelle)

    def __is_heap(self, node: Node) -> bool:
        if node == self.sentinelle:
            return True

        try:
            heap_left = node.value >= node.left.value
        except TypeError:
            heap_left = True

        try:
            heap_right = node.value >= node.right.value
        except TypeError:
            heap_right = True

        return (
            heap_left
            and heap_right
            and self.__is_heap(node.left)
            and self.__is_heap(node.right)
        )

    def is_heap(self) -> bool:
        return self.__is_heap(self.root())

    def lca(self, a: int, b: int) -> int:
        path_a = self.path(a, self.root())
        path_b = self.path(b, self.root())
        i = 0
        la = len(path_a)
        lb = len(path_b)
        while i < la and i < lb and path_a[i] == path_b[i]:
            i += 1
        return path_a[i - 1]

    def path(
        self, x: int, node: Node
    ):  # Shamelessly stolen on SO (https://stackoverflow.com/a/49227659/16027155)
        if node == self.sentinelle:
            return []
        if node.value == x:
            return [x]
        res = self.path(x, node.left)
        if res:  # If a path has been found
            return [node.value] + res
        res = self.path(x, node.right)
        if res:
            return [node.value] + res
        return []

    def __is_bst(self, node: Node):
        if node == self.sentinelle:
            return True

        try:
            bst_left = node.value >= node.left.value
        except TypeError:
            bst_left = True

        try:
            bst_right = node.value < node.right.value
        except TypeError:
            bst_right = True

        return (
            bst_left
            and bst_right
            and self.__is_bst(node.left)
            and self.__is_bst(node.right)
        )

    def is_bst(self):
        return self.__is_bst(self.root())

    def __to_linkedlist(self, node: Node):
        if node == self.sentinelle:
            return LinkedList()
        middle = LinkedList()
        middle.append(node.value)
        return (
            self.__to_linkedlist(node.left)
            .extend(middle)
            .extend(self.__to_linkedlist(node.right))
        )

    def to_linkedlist(self):
        return self.__to_linkedlist(self.root())


if __name__ == "__main__":
    t1 = BinaryTree([4, 2, 6])
    print(t1.to_linkedlist())
