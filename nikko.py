"""
ASSIGNMENT 12B: SPRINT 5 - DATA PERSISTENCE
Project: Sandwich Order System V5
"""

# constants
ORDER_HISTORY = "order_history.txt"

SIZES = ("6 inch", "12 inch")
PRICES = {"6 inch": 5.00, "12 inch": 8.00}
BREAD = ("White", "Wheat", "Italian", "Multigrain", "Sourdough")
PROTEIN = ("Turkey", "Ham", "Pepperoni", "Chicken", "Steak", "None")
CHEESE = ("American", "Swiss", "Cheddar", "Provolone", "None")
TOPPINGS = ("Lettuce", "Tomato", "Onion", "Pickles", "None")
SAUCES = ("Mayo", "Mustard", "Ranch", "None")

# functions


def lookup():
    fname = input("Please enter first name: ").strip().title()
    lname = input("Please enter last name: ").strip().title()
    phone_number = input("Please enter phone number: ")
    customer = fname + lname

    return fname, lname, phone_number


def take_order():
    # collects sandwich order information: bread, protein, cheese, toppings, sauce
    num = 1

    for size, price in PRICES.items():
        print(f"{num}.) Size: {size} | Price ${price}")
        num += 1
    num = 1
    try:
        my_size = int(
            input("Please enter the number of your sandwich size:  "))
    except Exception as e:
        print("Invalid input, defaulting to 6 inch.")
        my_size = 1
        print(e)

    for bread in BREAD:
        print(f"{num}.)  {bread}")
        num += 1
    num = 1
    try:
        my_bread = int(input("Please enter the number of your bread:  "))
    except Exception as e:
        print("Invalid input, defaulting to white bread.")
        my_bread = 1
        print(e)

    for protein in PROTEIN:
        print(f"{num}.)  {protein}")
        num += 1
    num = 1
    try:
        my_protein = int(input("Please enter the number of your protein:  "))
    except Exception as e:
        print("Invalid input, defaulting to turkey.")
        my_protein = 1
        print(e)

    for cheese in CHEESE:
        print(f"{num}.)  {cheese}")
        num += 1
    num = 1
    try:
        my_cheese = int(input("Please enter the number of your cheese:  "))
    except Exception as e:
        print("Invalid input, defaulting to american.")
        my_cheese = 1
        print(e)

    for topping in TOPPINGS:
        print(f"{num}.)  {topping}")
        num += 1
    num = 1
    try:
        my_topping = int(input("Please enter the number of your topping:  "))
    except Exception as e:
        print("Invalid input, defaulting to lettuce.")
        my_topping = 1
        print(e)

    for sauce in SAUCES:
        print(f"{num}.)  {sauce}")
        num += 1
    num = 1
    try:
        my_sauce = int(input("Please enter the number of your sauce:  "))
    except Exception as e:
        print("Invalid input, defaulting to mayo.")
        my_sauce = 1
        print(e)

    return (SIZES[my_size - 1], BREAD[my_bread - 1], PROTEIN[my_protein - 1],
            CHEESE[my_cheese - 1], TOPPINGS[my_topping - 1],
            SAUCES[my_sauce - 1])


def preview_order(order):
    (size, bread, protein, cheese, topping, sauce) = order

    print("\n--- ORDER PREVIEW ---")
    print(f"Size: {size}")
    print(f"Bread: {bread}")
    print(f"Protein: {protein}")
    print(f"Cheese: {cheese}")
    print(f"Topping: {topping}")
    print(f"Sauce: {sauce}")


def calculate_total(order):
    size = order[0]
    total = PRICES[size]

    print(f"\nTotal: ${total:.2f}")
    return total


def edit_order():
    print("\nEditing order")
    return take_order()


def delete_order():
    print("\nOrder has been canceled.")


def save_data_and_ticket(fname, lname, phone_number, order, total):
    (size, bread, protein, cheese, topping, sauce) = order

    # Save to file
    with open(ORDER_HISTORY, "a") as file:
        file.write("ORDER:\n")
        file.write(f"Name: {fname} {lname}\n")
        file.write(f"Phone: {phone_number}\n")
        file.write(f"Size: {size}\n")
        file.write(f"Bread: {bread}\n")
        file.write(f"Protein: {protein}\n")
        file.write(f"Cheese: {cheese}\n")
        file.write(f"Topping: {topping}\n")
        file.write(f"Sauce: {sauce}\n")
        file.write(f"Total: ${total:.2f}\n\n")

    # Print ticket
    print("\nFINAL TICKET")
    print(f"Customer: {fname} {lname}")
    print(f"Phone: {phone_number}")
    print(f"Size: {size}")
    print(f"Bread: {bread}")
    print(f"Protein: {protein}")
    print(f"Cheese: {cheese}")
    print(f"Topping: {topping}")
    print(f"Sauce: {sauce}")
    print(f"Total: ${total:.2f}")
    print("Order saved successfully.")


def main():

    # 1 Customer info and lookup
    fname, lname, phone_number = lookup()

    # 2 Taking order
    order = take_order()

    # 3 Preview order
    preview_order(order)

    # 4 Calculating total
    total = calculate_total(order)

    # 5 Confirm Order
    print("(C) Confirm Order")
    print("(E) Edit Order")
    print("(D) Delete Order")

    choice = input("Select an option: ").upper().strip()

    if choice == "E":
        order = edit_order()
        preview_order(order)
        total = calculate_total(order)

    elif choice == "D":
        delete_order()
        return
    else:
        # 6 Save order and print ticket
        save_data_and_ticket(fname, lname, phone_number, order, total)


main()
