class Coffee:
    # constructor to instantiate coffee with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Order:
    # constructor to instantiate customer's order with empty list
    def __init__(self):
        self.drinks = []
    
    # func to add a drink to customer's order
    def add_drink(self, coffee):
        self.drinks.append(coffee)
        if coffee.name.strip().lower() == "chai tea":
            print("\nWhat did you just say??? Chai TEA!?!? Chai means tea bro! You're saying tea tea. Would I ask you for a coffee coffee with room for cream cream?")
        else:
            print(f"\nGreat choice! One {coffee.name} coming right up.")
    
    # func to calculate total price
    def total(self):
        return sum(drink.price for drink in self.drinks)
    
    # func to show order summary
    def show_order(self):
        if not self.drinks:
            print("\nThere are no items in your order yet but you already knew that... c'mon move it or lose it rooster")
            return
        
        print("\nHere is your current order:")
        for i, drink in enumerate(self.drinks, 1):
            print(f"{i}. {drink.name} - ${drink.price}")
        
        print(f"\nYour total will be ${self.total()}\n All proceeds will contribute to the Save_Samuel's_Dreams_Fund.")
    
    # func to handle customer's checkout process
    def checkout(self):
        if not self.drinks:
            print("\nYour cart is empty. Whatchu waiting for? C'mon Lee!")
            return
        
        self.show_order()
        
        confirmation = input("\nAre you ready to proceed to checkout? (yes/no) ").strip().lower()
        
        if confirmation == "yes":
            print("\nOrder confirmed! Your drinks will be ready in a jiffy! Thank you!")
            self.drinks.clear()
        
        else:
            print("Checkout cancelled.")