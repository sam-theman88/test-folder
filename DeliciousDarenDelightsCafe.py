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
        
        print(f"\nYour total will be ${self.total()}\nAll proceeds will contribute to the Save_Samuel's_Dreams_Fund.")
    
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
            print("\nCheckout cancelled.")

# main method to start cafe app by displaying menu and handling user input
def main():
    
    menu = [
        Coffee("Espresso", 3.5),
        Coffee("Latte", 6),
        Coffee("Cappuccino", 5.5),
        Coffee("Americano", 3.5),
        Coffee("Chai tea", 5.75)
    ]
    
    order = Order()
    
    # print greeting
    print("\nTop of the morning to you dear lad! I'm Harry Longbottom and I'll be your barista for today, how may I be of service?")
    
    # handles user interaction
    while True:
        print("\n--- Coffee Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        
        print("-----------")
        print("6. View Order")
        print("7. Checkout")
        print("8. Exit")
        
        choice = int(input("\nWhich option tickles your fancy? "))
        
        if choice in [1, 2, 3, 4, 5]:
            order.add_drink(menu[choice - 1])
        elif choice == 6:
            order.show_order()
        elif choice == 7:
            order.checkout()
        elif choice == 8:
            print("\nThanks for visiting. Have a great day ahead :)")
            break
        else:
            print("\nInvalid choice. Please choose a valid number from the menu.")

# executes main method when app is opened
if __name__ == "__main__":
    main()
