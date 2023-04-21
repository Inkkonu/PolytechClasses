from tp5.binary_tree import BinaryTree
from tp5.node import Node


class BinarySearchTree(BinaryTree):

    def __lookup_rec(self, node: Node, key: int):
        if node == self.sentinelle or node.value is None:
            return None
        if node.value == key:
            return node
        if key <= node.value:
            return self.__lookup_rec(node.left, key)
        else:
            return self.__lookup_rec(node.right, key)

    def lookup_rec(self, key: int):
        return self.__lookup_rec(self.root(), key)

    def lookup_it(self, key: int):
        node = self.root()
        while node != self.sentinelle and node.value is not None:
            if node.value == key:
                return node
            if key <= node.value:
                node = node.left
            else:
                node = node.right
        return node

    def __insert(self, node: Node, key: int):
        if key <= node.value:
            if node.left == self.sentinelle:
                node.left = Node(key, node, self.sentinelle, self.sentinelle)
            else:
                self.__insert(node.left, key)
        else:
            if node.right == self.sentinelle:
                node.right = Node(key, node, self.sentinelle, self.sentinelle)
            else:
                self.__insert(node.right, key)

    def insert(self, key: int):
        self.__insert(self.root(), key)
        return self

    def remove(self, key: int):
        node = self.lookup_it(key)
        if key > self.root().value:
            node.parent.right = node.left
            node.parent.right.right = node.right
        elif key <= self.root().value:
            node.parent.left = node.right
            node.parent.left.left = node.left
        return self


if __name__ == '__main__':
    bst = BinarySearchTree([4, 2, 6])
    print(bst.to_linkedlist())
