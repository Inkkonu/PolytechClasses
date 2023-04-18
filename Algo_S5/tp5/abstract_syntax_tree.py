from tp5.binary_tree import BinaryTree
from tp5.node import Node


class AbstractSyntaxTree(BinaryTree):

    def eval(self):
        while self.height == 1:
            leafs = self.get_leafs()



    def __get_leafs(self, node: Node):
        if node.left == self.sentinelle and node.right == self.sentinelle:
            return [node]
        else:
            return self.__get_leafs(node.left) + self.__get_leafs(node.right)

    def get_leafs(self):
        return self.__get_leafs(self.root())


if __name__ == '__main__':
    ast = AbstractSyntaxTree([4, 2, 6, 5, 7])
    print(ast.get_leafs())
    for n in ast.get_leafs():
        print(n.value)
