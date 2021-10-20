import unittest
from src.pub import Pub
from src.customer import CustomerDetails
from src.drink import Drink


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.drink = Drink("vodka", 5, 2)
        self.customer = CustomerDetails("Iain", 50, 25, 0)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        
    def test_till_total_cash(self):
        self.assertEqual(1000, self.pub.till)

    def test_add_to_drinks_list(self):
        self.pub.add_to_drinks_list("vodka")
        self.assertEqual(1, len(self.pub.drinks))

    def test_remove_from_drinks_list(self):
        self.pub.add_to_drinks_list("vodka")
        self.pub.remove_from_drinks_list("vodka")
        self.assertEqual(0, len(self.pub.drinks))
        
    def test_update_till_total(self):
        self.pub.update_till_total(self.drink.price)
        self.assertEqual(1005, self.pub.till)
        
    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer.age))
    
    