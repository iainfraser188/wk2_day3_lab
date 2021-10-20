import unittest
from src.customer import CustomerDetails

class TestCustomerDetails(unittest.TestCase):
    def setUp(self):
        self.customer = CustomerDetails("Iain", 50)


    def test_customer_has_name(self):
        self.assertEqual("Iain", self.customer.name)
    
    def test_customer_has_money(self):
        self.assertEqual(50, self.customer.wallet)
        
    def test_add_to_drinks_bought(self):
        self.customer.add_to_drinks_bought("vodka")
        self.assertEqual(1, len(self.customer.drinks_bought))
        
    def update_wallet_total(self):
        self.update_wallet_total(self.price)
        self.assertEqual(45, self.customer.wallet)