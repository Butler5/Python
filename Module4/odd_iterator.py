class OddIterator:
    def __init__(self, it):
        self.it = iter(it)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            val = next(self.it)
            if val % 2 != 0:
                return val