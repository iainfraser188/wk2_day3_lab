import unittest
from src.pub import Pub
from src.customer import CustomerDetails


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.customer = CustomerDetails("Iain", 50)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        
    def test_till_total_cash(self):
        self.assertEqual(1000, self.pub.till)

    def test_customer_has_name(self):
        self.assertEqual("Iain", self.customer.name)
        
    def test_customer_has_money(self):
        self.assertEqual(50, self.customer.wallet)