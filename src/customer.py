class CustomerDetails:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks_bought = [] 
        
    def add_to_drinks_bought(self, drink_added):
        return self.drinks_bought.append(drink_added)
    
    def update_wallet_total(self, drink_price):
        self.wallet = self.wallet - drink_price