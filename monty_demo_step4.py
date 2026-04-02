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

    # TODO - change input to right after each menu displays

    # 1. Display Coffee Types
    print("\n--- DRINK TYPES ---")
    for i, coffee in enumerate(COFFEE, 1):
        print(f"{i}.) {coffee}")

    # 2. Display Sizes and Prices
    print("\n--- SIZES ---")
    # Using a list to allow numeric selection from the dictionary
    size_list = list(PRICES.keys())
    for i, size in enumerate(size_list, 1):
        print(f"{i}.) {size:12} | ${PRICES[size]:.2f}")

    # 3. Display Milk Options
    print("\n--- MILK OPTIONS ---")
    for i, milk in enumerate(MILKS, 1):
        print(f"{i}.) {milk}")

    # 4. Display Flavor Options
    print("\n--- FLAVOR ADD-INS ---")
    for i, flavor in enumerate(FLAVORS, 1):
        print(f"{i}.) {flavor}")

    # 5. Display Shot Strength
    print("\n--- SHOT STRENGTH ---")
    for i, shot in enumerate(SHOTS, 1):
        print(f"{i}.) {shot}")

    try:
        print("\n--- FINALIZING SELECTION ---")
        drink_idx = int(input("Select Drink Number: ")) - 1
        size_idx = int(input("Select Size Number: ")) - 1
        milk_idx = int(input("Select Milk Number: ")) - 1
        flavor_idx = int(input("Select Flavor Number: ")) - 1
        shot_idx = int(input("Select Shot Strength: ")) - 1

        # Map indices back to names for confirmation
        selected_drink = COFFEE[drink_idx]
        selected_size = size_list[size_idx]
        selected_milk = MILKS[milk_idx]
        selected_flavor = FLAVORS[flavor_idx]
        selected_shot = SHOTS[shot_idx]

        print(
            f"\nOrder Summary: {selected_size} {selected_drink} with {selected_milk} milk, {selected_flavor} flavor, ({selected_shot})")

        return selected_drink, selected_size, selected_milk, selected_flavor, selected_shot

    except Exception as e:
        print(f"Input Error: {e}")
        return None, None, None, None, None


def read_orders():
    # Placeholder for next week: Read file to display last 5 unique orders
    pass


def save_orders():
    # Placeholder for next week: Write current order to file
    print("Saving Order to File...")


def print_labels():
    print("Printing 2x3 Avery Label...")


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

    # If a valid selection was made, run the next steps
    if coffee:
        calculate_cost(size)
        print_labels()
        # save_orders()  <-- Ready for next week


main()
