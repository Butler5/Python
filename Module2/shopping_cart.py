class ShoppingCart:
    def __init__(self):
        self._items = {}

    def get_total_item_count(self):
        return sum(self.items.values())

    def get_item_count(self, item):
        return self._items[item] if item in self._items else 0

    def add_item(self, item, quantity):
            self._items[item] = self.get_item_count(item) + quantity

