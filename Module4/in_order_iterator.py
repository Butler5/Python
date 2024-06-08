class InOrderIterator:
    def __init__(self, root):
        self.iterable = []
        self.left_child(root)

    def __iter__(self):
        return self

    def left_child(self, current):
        while current is not None:
            self.iterable.append(current)
            current = current.left

    def __next__(self):
        return len(self.iterable) > 0

    def right_child(self):
        current = self.iterable.pop()
        if current.right is not None:
            self.left_child(current.right)
        return current
