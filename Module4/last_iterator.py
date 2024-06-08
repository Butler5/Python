class LastIterator:
    def __init__(self, it, count):
        self.it = iter(it)
        self.count = count
        self.list = []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.list:
            for item in self.it:
                self.list.append(item)
                if len(self.list) > self.count:
                    self.list.pop(0)
        return self.list.pop(0)
