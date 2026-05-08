# Commented Shopping Cart Program


import json
import os

TARGET = 'student_repo'

class ShoppingCart:

    # Create a new shopping cart.
    # Each cart has a name and a list of Item objects.
    def __init__(self, name):
        self._name = name
        self._items = []

    # String representation of the shopping cart.
    def __str__(self):
        return f'The name of my shopping cart is {self.name}'

    # Read-only property for cart name.
    @property
    def name(self):
        return self._name

    # Property for the list of items in the cart.
    @property
    def items(self):
        return self._items

    # Setter for items list.
    @items.setter
    def items(self, items):
        self._items = items

    # Display all items currently in the cart.
    def displayCart(self):

        print('Your shopping cart contains: \n\n')

        # If the cart contains items, display them.
        if self.items:
            for i, item in enumerate(self.items):
                print(f'({i+1}): {item.quantity} {item.description} ${item.price:>10.2f}')

        # Otherwise display that the cart is empty.
        else:
            print('Your cart is empty\n\n')


    def getItemNumber(self):
        # TODO
      
        return 1   # return item_no 
    def getQuantity(self):
        txt = 'How many would you like to buy or x to exit: '
        while True:
            try:
                quantity = input(txt)
                if quantity.lower() == 'x': return
                quantity = int(quantity)
                if quantity < 1: raise ValueError
                break
            except ValueError:
                txt = 'Please enter a positive integer for quantity\n\n or x to exit: '

        return quantity

    # Allow the user to buy an item and add it to the cart.
    def buyItem(self, inventory):

        # Display available inventory.
        displayInventory(inventory)
        print()

        item_no = self.getItemNumber()
        quantity = self.getQuantity()

        if item_no == None or quantity == None: return
        

        # Retrieve item information from inventory.
        description = inventory[item_no]['description']
        price = inventory[item_no]['price']

        # Create Item object.
        item = Item(quantity, description, price)

        # Add item to cart.
        self.items.append(item)

        # TODO Maintain the No-Duplicate-Items Cart Invariant

    # Compute total cost and empty the cart.
    def checkOut(self):

        total = 0

        # TODO Sum the total value of all items.
        

        print(f'Please pay the sum of ${total:.2f}')

        # TODO Empty the shopping cart after checkout.
        


class Item:

    # Create a new item.
    def __init__(self, quantity, description, price):
        self._quantity = quantity
        self._description = description
        self._price = price

    # String representation of item.
    def __str__(self):
        return f'I have {self.quantity} {self.description} at ${self.price:.2f}'
    
    def __add__(self, other):
        # TODO
        pass

    # Quantity property.
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    # Description property.
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    # Price property.
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


# Clear terminal screen.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Load store inventory from JSON file.
def loadInventory():

    with open(f"C:/PythonClass/{TARGET}/final_exam/inventory.json", "r") as f:
        inventory = json.load(f)

    inventory_int_keys = {}
    for key, value in inventory.items():        
        inventory_int_keys[int(key)] = value

    return inventory_int_keys


# Display inventory items.
def displayInventory(inventory):

    print(f"{'Babson Store front':^60}")
    print("-" * 60)
    print(f"Item #             {'Description':^20}            Price")
    print("-" * 60)
    print()

    cnt = 1

    for product in inventory.values():

        print(f"{cnt:>4}:             {product['description']:<20}           ${product['price']:>6.2f}")
        cnt += 1


# Load shopping carts from JSON and reconstruct objects.
def loadShoppingCarts():

    with open(f"C:/PythonClass/{TARGET}/final_exam/inventory.json", "r") as f:
        carts = json.load(f)

    # Dictionary that will contain ShoppingCart objects.
    shoppingcarts = {}

    # Rebuild ShoppingCart and Item objects.
    for cart_name in carts:

        shoppingcart = ShoppingCart(cart_name)

        for item_dict in carts[cart_name]:

            item = Item(
                item_dict["quantity"],
                item_dict["description"],
                item_dict["price"]
            )

            shoppingcart.items.append(item)

        shoppingcarts[cart_name] = shoppingcart

    return shoppingcarts


# Convert ShoppingCart objects into dictionaries and store them.
def storeShoppingCarts(shoppingcarts):

    carts = {}

    for key in shoppingcarts:

        items = []

        for item in shoppingcarts[key].items:

            item_dict = {
                "quantity": item.quantity,
                "description": item.description,
                "price": item.price
            }

            items.append(item_dict)

        carts[key] = items

    with open(f"C:/PythonClass/{TARGET}/final_exam/inventory.json", "r") as f:
        json.dump(carts, f, indent=2)


# Load an existing shopping cart or create a new one.
def cartName(shoppingcarts):

    while True:

        txt = 'Load existing cart or create new cart (load/new) ?: '
        cart_status = input(txt).lower()

        if cart_status in ['load', 'new']:

            while True:

                txt = 'Please enter the name of your shopping cart or 9 to go back: '
                cart_name = input(txt)

                # Return to previous menu.
                if cart_name == '9':
                    break

                # Load existing cart.
                if cart_status == 'load':

                    if cart_name not in shoppingcarts:
                        print('The shopping cart was not found, try again')

                    else:
                        return shoppingcarts[cart_name]

                # Create a new cart.
                elif cart_status == 'new':

                    if cart_name in shoppingcarts:
                        print('That shopping cart is being used, try again')

                    else:
                        shoppingcart = ShoppingCart(cart_name)

                        shoppingcarts[cart_name] = shoppingcart

                        return shoppingcart


# Main menu loop for the shopping application.
def shoppingMenu():

    # Load shopping carts and inventory.
    shoppingcarts = loadShoppingCarts()
    inventory = loadInventory()

    # Select or create cart.
    shoppingcart = cartName(shoppingcarts)

    while True:

        # Display current cart contents.
        shoppingcart.displayCart()

        # Menu depends on whether cart is empty.
        if shoppingcart.items:
            txt = '1. Buy Item\n2. Checkout\nor x to Exit\n\nEnter choice: '

        else:
            txt = '1. Buy Item\nor x to Exit\n\nEnter choice: '

        # Validate menu choice.
        while True:

            try:
                choice = input(txt)

                # Exit program.
                if choice.lower() == 'x':
                    return

                choice = int(choice)
                break

            except ValueError:
                pass

        # Buy item.
        if choice == 1:
            shoppingcart.buyItem(inventory)
            # make sure dictionary points to the updated cart
            shoppingcarts[shoppingcart.name] = shoppingcart
            storeShoppingCarts(shoppingcarts)

        # Checkout.
        elif choice == 2:
            shoppingcart.checkOut()
            # make sure dictionary points to the updated emptied cart
            shoppingcarts[shoppingcart.name] = shoppingcart
            storeShoppingCarts(shoppingcarts)


# Start the program.
shoppingMenu()

'''
TODO
1) State: What is the main state of the shopping cart program? Be specific about which information changes over time.



2) Transitions: Which methods change the state of a shopping cart? Briefly explain what each transition does.



3) Invariant: What invariant does your completed cart maintain? How does your code preserve that invariant?



4) Data representation: Explain the difference between the runtime representation of a shopping cart and the JSON representation stored in shopping_carts.json.



5) Inventory representation: Why does the program convert inventory keys from strings to integers when loading inventory.json?



6) Responsibility: Why is the duplicate-item search logic placed in ShoppingCart.buyItem() instead of inside Item.__add__()?



7) AI control: Give one example where you corrected, limited, tested, or redirected AI output.


'''

