from binary_tree import BinaryTreeNode
from binary_tree import BinaryTree


class PreOrderIterator:
    def __init__(self):
        self.n = 1
        self.current_node = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current_node
        self.current_node

    def preOrderIterator(self):
        if self is None:
            return
        print(self.value, end=" ")

        PreOrderIterator.iterator(self._left_child)

        PreOrderIterator.iterator(self._right_child)


if __name__ == '__main__':
    n1 = BinaryTreeNode("A")
    n2 = BinaryTreeNode("B")
    n3 = BinaryTreeNode("C", n1, n2)
    n4 = BinaryTreeNode("D")
    n5 = BinaryTreeNode("E", n4, n3)
    n6 = BinaryTreeNode("F", n5)
    n7 = BinaryTreeNode("G")
    n8 = BinaryTreeNode("H", n6, n7)
    tree = BinaryTree(n8)
    print(tree.root.value)
    print(tree.root.left_child.left_child.value)
