import unittest
from src.customer import CustomerDetails
from src.drink import Drink

class TestCustomerDetails(unittest.TestCase):
    def setUp(self):
        self.customer = CustomerDetails("Iain", 50)
        self.drink = Drink("vodka", 5)


    def test_customer_has_name(self):
        self.assertEqual("Iain", self.customer.name)
    
    def test_customer_has_money(self):
        self.assertEqual(50, self.customer.wallet)
        
    def test_add_to_drinks_bought(self):
        self.customer.add_to_drinks_bought("vodka")
        self.assertEqual(1, len(self.customer.drinks_bought))
        
    def test_update_wallet_total(self):
        self.customer.update_wallet_total(self.drink.price)
        self.assertEqual(45, self.customer.wallet)