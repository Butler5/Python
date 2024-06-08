class PostOrderIterator:
    def __init__(self, root):
        self.iterable = []
        self.right_child(root)

    def __iter__(self):
        return self

    def right_child(self, current):
        while current is not None:
            self.iterable.append(current)
            current = current.right

    def __next__(self):
        return len(self.iterable) > 0

    def left_child(self):
        current = self.iterable.pop()
        if current.left is not None:
            self.right_child(current.right)
        return current