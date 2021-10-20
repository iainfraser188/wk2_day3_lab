class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []   
    
    def add_to_drinks_list(self, drink_name_added):
        return self.drinks.append(drink_name_added)
    
    def remove_from_drinks_list(self, drink_name_remove):
        return self.drinks.remove(drink_name_remove)
        
    def update_till_total(self, drink_price):
        self.till = self.till + drink_price