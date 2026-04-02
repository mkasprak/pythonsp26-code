"""
    Write to files
"""

"""
1. Demonstrate functions
2. Interface design (menus/ passing)
"""

COFFEE = ("Espresso", "Americano", "Latte", "Cappuccino",
          "Macchiato", "Mocha", "Flat White", "TEA", "COCOA")

PRICES = {
    "Small": 3.00,
    "Medium": 4.00,
    "Large": 5.00,
    "Extra Large": 6.00
}

MILKS = ("Soy", "Oat", "Whole", "Coconut", "2%", "None")

FLAVORS = ("Vanilla", "Caramel", "Hazelnut", "Mocha",
           "Peppermint", "Pumpkin Spice", "Sugar Free Vanilla", "None")

SHOTS = ("Normal: 6", "Light: 3", "Heavy: 9")


def lookup():
    """Collects employee identification details."""
    fname = input("Please Enter First Name: ")
    lname = input("Please Enter your Last Name: ")
    extension = input("Please enter your extension: ")
    emp_num = input("Please enter your employee number: ")

    return fname, lname, extension, emp_num


def ordering_system():
    """Displays menus and captures all user selections for the drink."""
    try:
        # TODO - change input to right after each menu displays

        # 1. Display Coffee Types
        print("\n--- DRINK TYPES ---")
        for i, coffee in enumerate(COFFEE, 1):
            print(f"{i}.) {coffee}")
        drink_idx = int(input("Select Drink Number: ")) - 1

        # 2. Display Sizes and Prices
        print("\n--- SIZES ---")
        # Using a list to allow numeric selection from the dictionary
        size_list = list(PRICES.keys())
        for i, size in enumerate(size_list, 1):
            print(f"{i}.) {size:12} | ${PRICES[size]:.2f}")
        size_idx = int(input("Select Size Number: ")) - \
            1  # -1 because we count from 0

        # 3. Display Milk Options
        print("\n--- MILK OPTIONS ---")
        for i, milk in enumerate(MILKS, 1):
            print(f"{i}.) {milk}")
        milk_idx = int(input("Select Milk Number: ")) - 1

        # 4. Display Flavor Options
        print("\n--- FLAVOR ADD-INS ---")
        for i, flavor in enumerate(FLAVORS, 1):
            print(f"{i}.) {flavor}")
        flavor_idx = int(input("Select Flavor Number: ")) - 1

        # 5. Display Shot Strength
        print("\n--- SHOT STRENGTH ---")
        for i, shot in enumerate(SHOTS, 1):
            print(f"{i}.) {shot}")
        shot_idx = int(input("Select Shot Strength: ")) - 1

        # Map indices back to names for confirmation
        drink = COFFEE[drink_idx]
        size = size_list[size_idx]
        milk = MILKS[milk_idx]
        flavor = FLAVORS[flavor_idx]
        shot = SHOTS[shot_idx]

        print(
            f"\n{size} {drink} with {milk} milk, shots {shot} of {flavor}")

        return drink, size, milk, flavor, shot

    except Exception as e:
        print(f"Input Error: {e}")
        return None, None, None, None, None


def read_orders():
    # Placeholder for next week: Read file to display last 5 unique orders
    pass


def save_orders(first, last, ext, coffee, size, milk, flavor, shots):
    with open("orders.txt", "a") as file:
        file.write(
            f"{first}, {last}, {coffee}, {size}, {milk}, {flavor}, {shots}")


def print_labels(first, last, coffee, size, milk, flavor, shots, cost):
    print(f"{first} {last}\nDrink: {coffee}\nSize: {size}\Milk Type:{milk}")
    print(f"Flavor: {flavor}, Number of pumps: {shots}")


def calculate_cost(size_name):
    """Calculates total based on the selected size key."""
    if size_name in PRICES:
        cost = PRICES[size_name]
        print(f"Total Cost for paycheck deduction: ${cost:.2f}")
    else:
        print("Cost calculation unavailable.")


def main():
    # User Lookup
    first, last, ext, emp = lookup()

    # Run Ordering Menu
    coffee, size, milk, flavor, shots = ordering_system()
    save_orders(first, last, ext, coffee, size, milk, flavor, shots)

    # If a valid selection was made, run the next steps
    if coffee:
        cost = calculate_cost(size)
        print_labels(first, last, coffee, size, milk, flavor, shots, cost)
        # save_orders()  <-- Ready for next week


main()
