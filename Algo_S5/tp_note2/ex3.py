from __future__ import annotations
from données2 import listePrevert


# Question 3.1

class Node:

    def __init__(self, mot: str, nbOcc: int, nodeLeft: Node, nodeRight: Node):
        self.mot = mot
        self.nbOcc = nbOcc
        self.left = nodeLeft
        self.right = nodeRight


class Tree:

    def __init__(self, root: Node):
        self.root = root

    # Question 3.2

    def ajouter_mot(self, mot: str):
        if self.root is None:
            self.root = Node(mot, 1, None, None)
            return self
        else:
            n = self.root
            n_parent = None
            while n is not None and n.mot != mot:
                if mot > n.mot:
                    n_parent = n
                    n = n.right
                elif mot < n.mot:
                    n_parent = n
                    n = n.left
            if n is not None:
                n.nbOcc += 1
            else:
                if mot > n_parent.mot:
                    n_parent.right = Node(mot, 1, None, None)
                else:
                    n_parent.left = Node(mot, 1, None, None)

    # Question 3.3
    # Réponse dans le main ci-dessous

    # Question 3.4

    def show(self):
        l = []
        if self.root is None:
            return l
        for t in self.to_tuple_list():  # Fonction définie dans la question juste après
            print(f'{t[0]} : {t[1]}')

    # Question 3.5

    def to_tuple_list(self):
        l = []
        if self.root is None:
            return l
        return sorted(self.__append(l, self.root),
                      key=lambda e: e[0])  # La liste étant une liste de tuples (mot, nbOcc), on la trie donc sur le mot

    def __append(self, l, node):
        l.append((node.mot, node.nbOcc))
        if node.left is not None and node.right is not None:
            self.__append(l, node.left) + self.__append(l, node.right)
        if node.right is None and node.left is not None:
            self.__append(l, node.left)
        if node.left is None and node.right is not None:
            self.__append(l, node.right)
        return l

    # Question 3.6

    def to_tuple_list_decreasing(self):
        return sorted(self.to_tuple_list(), key=lambda e: e[1], reverse=True)  # reverse=True pour l'ordre décroissant


if __name__ == '__main__':
    t = Tree(None)
    for mot in listePrevert:
        t.ajouter_mot(mot)
    t.show()
