# 4. Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.
class Cart:
    def __init__(self):
        self.items = {}
    
    def add_items(self, item_name, quantity=1):
        item_name = item_name.lower()
        if item_name in items:
            available_quantity = items[item_name]['quantity']
            if quantity > available_quantity:
                print(f"Only {available_quantity} of {item_name} available. Cannot add {quantity}.")
                return
            
            price = items[item_name]['price']
            if item_name in self.items:
                self.items[item_name]['quantity'] += quantity
            else:
                self.items[item_name] = {'price': price, 'quantity': quantity}
            
            # Update available quantity in the store after adding to the cart
            items[item_name]['quantity'] -= quantity
            
            print(f"Added {quantity} of {item_name} to the cart.")
        else:
            print(f"{item_name} is not available.")

    def remove_items(self, item_name, quantity):
        item_name = item_name.lower()
        if item_name in self.items:
            if self.items[item_name]['quantity'] <= quantity:
                # Restore the available quantity in the store
                items[item_name]['quantity'] += self.items[item_name]['quantity']
                
                del self.items[item_name]
                print(f"Removed all {item_name} from the cart.")
            else:
                self.items[item_name]['quantity'] -= quantity
                print(f"Removed {quantity} of {item_name} from the cart.")

                # Restore the available quantity in the store
                items[item_name]['quantity'] += quantity
                print(f"Removed {quantity} of {item_name} from the cart.")
        else:
            print(f"{item_name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total

    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item_name, details in self.items.items():
                print(f"{item_name}: ${details['price']} x {details['quantity']}")
            total = self.calculate_total()
            print(f"Total: ${total:.2f}")

items = {
    'apple': {'price': 0.5, 'quantity': 50},
    'banana': {'price': 0.3, 'quantity': 100},
    'orange': {'price': 0.8, 'quantity': 30},
    'milk': {'price': 1.5, 'quantity': 20},
    'bread': {'price': 2.0, 'quantity': 15}
}

def show_items(items):
    print("Available items:")
    for item_name, details in items.items():
        print(f"{item_name}: ${details['price']} (Quantity available: {details['quantity']})")


# List to add, remove the item that the user wants
user_cart = Cart()
show_items(items)

while True:
    u_choice = input('''To buy items type a
                    To remove from cart type r
                    To view your cart type c
                    To quit type q:  ''').lower()
    
    if u_choice == "a":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        user_cart.add_items(item_name, quantity)

    elif u_choice == "r":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        user_cart.remove_items(item_name, quantity)

    elif u_choice == "c":
        user_cart.show_cart()

    elif u_choice == "q":
        print("Thanks for shopping!")
        break

    else:
        print("Invalid input. Enter a to add, r to remove, c to view cart, or q to quit.")


