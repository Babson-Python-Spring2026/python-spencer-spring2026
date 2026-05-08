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
        # input validation — repeatedly ask until valid item number or x to cancel
        # user sees items 1-10 but inventory keys are 1001-1010
        # transition: converts user-facing number into runtime inventory key
        txt = 'Select an item number (1-10) or x to exit: '
        while True:
            try:
                choice = input(txt)
                if choice.lower() == 'x':
                    return None
                choice = int(choice)
                if choice < 1 or choice > 10:
                    raise ValueError
                # convert user-facing number to inventory key
                item_no = choice + 1000
                return item_no
            except ValueError:
                txt = 'Invalid choice. Enter a number 1-10 or x to exit: '
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

        # invariant: cart should never have two items with same description and price
        # search existing cart for a matching item
        # if found, combine using __add__ and replace the old item
        # if not found, just append normally
        found = False
        for i in range(len(self.items)):
            if self.items[i].description == item.description and self.items[i].price == item.price:
                self.items[i] = self.items[i] + item
                found = True
                break

        if not found:
            self.items.append(item)

    # Compute total cost and empty the cart.
    def checkOut(self):

        # state transition: cart with items -> empty cart
        # compute total by summing quantity * price for each item
        total = 0
        for item in self.items:
            total = total + (item.quantity * item.price)

        print(f'Please pay the sum of ${total:.2f}')

        # clear the cart — transition to empty state
        self.items = []


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
        # combine two compatible items into one with combined quantity
        # invariant: items must have same description and same price
        if self.description == other.description and self.price == other.price:
            return Item(self.quantity + other.quantity, self.description, self.price)
        else:
            raise ValueError("Items are not compatible")

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

    with open(os.path.join(os.path.dirname(__file__), "inventory.json"), "r") as f:
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

    with open(os.path.join(os.path.dirname(__file__), "shopping_carts.json"), "r") as f:
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

    with open(os.path.join(os.path.dirname(__file__), "shopping_carts.json"), "w") as f:
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

The main state is the shopping cart's list of Item objects. This list changes when the user
buys an item (an Item is added or an existing Item's quantity increases) and when the user
checks out (the list gets emptied). The shoppingcarts dictionary also changes when new carts
are created or existing ones are updated. The inventory does not change — it is fixed input.


2) Transitions: Which methods change the state of a shopping cart? Briefly explain what each transition does.

buyItem() — adds a new item to the cart or merges it with an existing item that has the
same description and price. This changes the items list.
checkOut() — computes the total cost and then empties the items list. The cart goes from
having items to being empty.


3) Invariant: What invariant does your completed cart maintain? How does your code preserve that invariant?

The cart never contains two Item objects with the same description and same price. In buyItem,
before appending, I search the existing items list. If I find a match, I use __add__ to combine
the quantities into one Item and replace the old one. If no match, I append normally. This
means duplicates are merged at the point of entry — they can never accumulate.


4) Data representation: Explain the difference between the runtime representation of a shopping cart and the JSON representation stored in shopping_carts.json.

At runtime, a shopping cart is a ShoppingCart object containing a list of Item objects. Each
Item has quantity, description, and price as attributes with properties and setters. In JSON,
carts are stored as a dictionary where each key is a cart name and each value is a list of
plain dictionaries with "quantity", "description", and "price" keys. JSON can only store simple
types (strings, numbers, lists, dicts) so the objects have to be converted to dicts for saving
and rebuilt into objects when loading.


5) Inventory representation: Why does the program convert inventory keys from strings to integers when loading inventory.json?

JSON object keys are always strings, so the keys come in as "1001", "1002", etc. The program
converts them to integers because integer keys make the item-number math simpler. The user
enters 1-10, and we add 1000 to get the inventory key (1001-1010). If the keys stayed as
strings we'd have to convert to string every time we look something up, which is messier.


6) Responsibility: Why is the duplicate-item search logic placed in ShoppingCart.buyItem() instead of inside Item.__add__()?

Item.__add__ only knows how to combine two items — it checks if they're compatible and returns
a new Item with the combined quantity. It doesn't know anything about the cart or what other
items are in it. The search logic (finding the duplicate in the cart) belongs in buyItem because
the cart owns the items list. The cart is responsible for maintaining its own invariant, just
like how in class the School enforced no-duplicate-IDs, not the Student.


7) AI control: Give one example where you corrected, limited, tested, or redirected AI output.

When AI first gave me the buyItem code, it just appended the new item without checking for
duplicates. I told it that wasnt right because the invariant says no duplicate items in the
cart. I explained that it needed to search the existing items first and use __add__ to merge
if a match was found. I had to specify the loop structure myself — iterate through self.items,
check description and price, and replace with the combined item if matched.

'''

