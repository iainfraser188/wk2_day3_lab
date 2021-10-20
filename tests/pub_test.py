import unittest
from src.pub import Pub
from src.customer import CustomerDetails
from src.drink import Drink


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.drink = Drink("vodka", 5)
    
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
        
    
    
    
    
    # def sell_pet_to_customer(pet_shop, pet, customer):
    # if pet != None and customer_can_afford_pet(customer, pet):
    #     remove_pet_by_name(pet_shop, pet["name"])
    #     add_pet_to_customer(customer, pet)
    #     remove_customer_cash(customer, pet["price"])
    #     add_or_remove_cash(pet_shop, pet["price"])
    #     increase_pets_sold(pet_shop, 1)