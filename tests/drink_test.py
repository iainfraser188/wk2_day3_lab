import unittest
from src.drink import Drink

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("vodka", 5)
        

    def test_what_to_drink(self):
        self.assertEqual("vodka", self.drink.name)
        
    def test_drink_price(self):
        self.assertEqual(5, self.drink.price)