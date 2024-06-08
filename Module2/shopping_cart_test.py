from shopping_cart import ShoppingCart
import unittest

class ShoppingCartTest(unittest.TestCase):

    def test_a_shopping_is_empty_when_first_created(self):
        """SPEC: a cart is empty when it is first created"""
        cart = ShoppingCart()
        some_item = "pickles"
        self.assertEqual(0, cart.get_total_item_count())
        self.assertEqual(0, cart.get_item_count(some_item))

    def test_adding_increases_occurrences(self):
        """SPEC: adding stock items increases the number of occurences of the stock item in the cart"""
        cart = ShoppingCart()
        item_1 = "pickles"
        quantity_1_1 = 10
        quantity_1_2 = 30
        item_2 = "oranges"
        quantity_2 = 37
        cart.add_item(item_1, quantity_1_1)
        cart.add_item(item_2, quantity_2)
        cart.add_item(item_1, quantity_1_2)
        self.assertEqual(quantity_1_1 + quantity_1_2, cart.get_item_count(item_1))
        self.assertEqual(quantity_2, cart.get_item_count(item_2))
        self.assertEqual(quantity_1_1 + + quantity_1_2 + quantity_2, cart.get_total_item_count())