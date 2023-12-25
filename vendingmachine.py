# a list of dictionaries representing the drinks menu
drinks_menu = [
    {
        'itemname': 'Mountain Dew',
        'itemno': 1,
        'price': 2,
        'qty': 4,
    },
    {
        'itemname': 'Thumbs Up',
        'itemno': 2,
        'price': 2,
        'qty': 5,
    },
    {
        'itemname': 'Coca Cola',
        'itemno': 3,
        'price': 2,
        'qty': 6,
    },
    {
        'itemname': 'Sparkling Water',
        'itemno': 4,
        'price': 6,
        'qty': 8,
    },
    {
        'itemname': 'Pepsi',
        'itemno': 5,
        'price': 2,
        'qty': 5,
    },
    {
        'itemname': 'Water',
        'itemno': 6,
        'price': 1,
        'qty': 7,
    },
    {
        'itemname': 'Strawberry Milk',
        'itemno': 7,
        'price': 3,
        'qty': 3,
    },
    {
        'itemname': 'Chocolate Milk',
        'itemno': 8,
        'price': 3,
        'qty': 2,
    },
    {
        'itemname': 'Apple Juice',
        'itemno': 9,
        'price': 2,
        'qty': 7,
    },
    {
        'itemname': 'Mango Juice',
        'itemno': 10,
        'price': 2,
        'qty': 4,
    },
    {
        'itemname': 'Cup Cake',
        'itemno': 11,
        'price': 3,
        'qty': 8,
    },
    {
        'itemname': 'Oatville Biscuit',
        'itemno': 12,
        'price': 3,
        'qty': 9,
    },
    {
        'itemname': 'Protein Bar',
        'itemno': 13,
        'price': 5,
        'qty': 8,
    },
    {
        'itemname': 'Oreo',
        'itemno': 14,
        'price': 2,
        'qty': 3,
    },
    {
        'itemname': 'Tomato Chips',
        'itemno': 15,
        'price': 1,
        'qty': 5,
    },
    {
        'itemname': 'Chilli Chips',
        'itemno': 16,
        'price': 1,
        'qty': 1,
    },
    {
        'itemname': 'Lotus Biscuit',
        'itemno': 17,
        'price': 3,
        'qty': 7,
    },
    {
        'itemname': 'Kit Kat',
        'itemno': 18,
        'price': 2,
        'qty': 9,
    },
    {
        'itemname': 'Snickers',
        'itemno': 19,
        'price': 2,
        'qty': 4,
    },
    {
        'itemname': 'Skittles',
        'itemno': 20,
        'price': 5,
        'qty': 9,
    },
]

# function to print drinks
def print_drinks():
    print("*********FarzeenMart-Vending-Machine*********")
    print("=====================DRINKS==================")
    for item in drinks_menu[:10]:  # Display only the first 10 items
        print(f" {item['itemno']:02} {item['itemname']:20} {item['price']} AED")

# function to print snacks
def print_snacks():
    print("=====================SNACKS==================")
    snacks_items = {
        "11 Cup Cake": "3 AED",
        "12 Oatville Biscuit": "3 AED",
        "13 Protein Bar": "5 AED",
        "14 Oreo": "2 AED",
        "15 Tomato Chips": "1 AED",
        "16 Chilli Chips": "1 AED",
        "17 Lotus Biscuit": "3 AED",
        "18 Kit Kat": "2 AED",
        "19 Snickers": "2 AED",
        "20 Skittles": "5 AED",
    }

    # a for loop system that prints out the dictionary like a menu
    for item, price in snacks_items.items():
        print(f" {item:30}, {price}")
    print()

# function to print the menu
def print_menu():
    print_drinks()
    print_snacks()

# function to calculate and print the receipt
def print_receipt(selected_item, remaining_balance):
    print("\n*********RECEIPT*********")
    print(f"Selected Item: {selected_item['itemname']}")
    print(f"Price: {selected_item['price']} AED")
    print(f"Remaining Balance: {remaining_balance:.2f} AED")

# function to process user's order
def order():
    # Print menu
    print_menu()

    # Get user budget
    user_budget = float(input("Enter the amount of AED you have: "))
    remaining_balance = user_budget

    # Get user order
    selected_item_no = int(input("Enter the item number you want to purchase: "))

    # Find the selected item in the menu
    selected_item = next((item for item in drinks_menu if item['itemno'] == selected_item_no), None)

    if selected_item:
        # Check if user can afford the selected item
        if remaining_balance >= selected_item['price']:
            remaining_balance -= selected_item['price']
            print_receipt(selected_item, remaining_balance)
        else:
            print("Insufficient funds. Cannot purchase the selected item.")
    else:
        print("Invalid item number. Please choose a valid item.")

# calling the order function
order()
