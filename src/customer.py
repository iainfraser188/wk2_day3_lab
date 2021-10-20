class CustomerDetails:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drinks_bought = [] 
        self.drunkeness = drunkeness
        
    def add_to_drinks_bought(self, drink_added):
        return self.drinks_bought.append(drink_added)
    
    def update_wallet_total(self, drink_price):
        self.wallet = self.wallet - drink_price
        
    def drunkeness_level(self, alcohol_level):
        self.drunkeness = self.drunkeness + alcohol_level

        
