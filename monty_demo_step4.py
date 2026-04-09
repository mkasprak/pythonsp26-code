"""
    Write to files
"""

"""
1. Demonstrate functions
2. Interface design (menus/ passing)
"""


def lookup():
    """Collects employee identification details."""
    fname = input("Please Enter First Name: ")
    lname = input("Please Enter your Last Name: ")
    extension = input("Please enter your extension: ")
    emp_num = input("Please enter your employee number: ")

    return fname, lname, extension, emp_num


def read_menu():
    """ read_menu will import menu.txt and pull it into a list. We can then
        break down the list into the specific variables and
        dictionaries that we need. """
    menus = {}
    try:
        # open and read file
        with open("menu.txt", 'r') as file:
            for line in file:
                parts_of_line = line.strip().split(';')
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

        # for x, y in menus.items():
        #     print(x, y)
        return menus
    except Exception as e:
        print(e)


def split_into_variables(menu_items):
    """break the menu file into separate variables"""
    print("In split_into_variables")

    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")

    return coffee, prices, milks, flavors, shots


def ordering_system(coffee_menu, prices_menu, milks_menu,
                    flavors_menu, shots_menu):
    """Displays menus and captures all user selections for the drink."""

    # test prints
    print("Test ordering system")
    print(f"drinks: {coffee_menu}\nprices: {prices_menu}\nmilks:{milks_menu}")
    print(f"flavors: {flavors_menu}\nshots: {shots_menu}")
    try:
        # TODO - change input to right after each menu displays
        nbr = 1
        # 1. Display coffee Types
        print("\n--- DRINK TYPES ---")
        coffee_item = coffee_menu.split(',')
        for item in coffee_item:
            item = item.strip()
            print(f"\t{nbr}.  {item}")
            nbr += 1
        drink_idx = int(input("Select Drink Number: ")) - 1

        # 2. Display Sizes and prices
        print("\n--- SIZES ---")
        # Using a list to allow numeric selection from the dictionary
        print(prices_menu)
        nbr = 1
        size_item = prices_menu.split(',')
        for item, size in (size_item):
            print(f"\t{nbr}. {size:12} | ${prices_menu[size]:.2f}")
            nbr += 1
        size_idx = int(input("Select Size Number: ")) - \
            1  # -1 because we count from 0

        # 3. Display Milk Options
        print("\n--- MILK OPTIONS ---")
        nbr = 1
        milk_item = milks_menu.split(',')
        for i, milk in (milk_item):
            milk = milk.strip()
            print(f"\t{nbr}. {milk}")
            nbr += 1
        milk_idx = int(input("Select Milk Number: ")) - 1

        # 4. Display Flavor Options
        print("\n--- FLAVOR ADD-INS ---")
        nbr = 1
        flavor_item = flavors_menu.split(',')
        for flavor in (flavor_item):
            flavor = flavor.strip()
            print(f"\t{nbr}. {flavor}")
            nbr += 1
        flavor_idx = int(input("Select Flavor Number: ")) - 1

        # 5. Display Shot Strength
        print("\n--- SHOT STRENGTH ---")
        nbr = 1
        shot_item = shots_menu.split(",")
        for shot in (shot_item):
            shot = shot.strip()
            print(f"{nbr}. {shot}")
        shot_idx = int(input("Select Shot Strength: ")) - 1

        # Map indices back to names for confirmation
        drink = coffee_menu[drink_idx]
        size = size_item[size_idx]
        milk = milks_menu[milk_idx]
        flavor = flavors_menu[flavor_idx]
        shot = shots_menu[shot_idx]

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
    print(f"{first} {last}\nDrink: {coffee}\nSize: {size}\nMilk Type:{milk}")
    print(f"Flavor: {flavor}, Number of pumps: {shots}")


def calculate_cost(size_name, prices_menu):
    """Calculates total based on the selected size key."""
    if size_name in prices_menu:
        cost = prices_menu[size_name]
        print(f"Total Cost for paycheck deduction: ${cost:.2f}")
    else:
        print("Cost calculation unavailable.")


def main():
    # User Lookup
    first, last, ext, emp = lookup()

    # read in external menu file
    menu_items = read_menu()

    coffee_menu, prices_menu, milks_menu, flavors_menu, shots_menu \
        = split_into_variables(menu_items)

    # Run Ordering Menu
    coffee_order, size_order, milk_order, flavor_order, shots_order = \
        ordering_system(coffee_menu, prices_menu, milks_menu,
                        flavors_menu, shots_menu)
    save_orders(first, last, ext, coffee_order, size_order,
                milk_order, flavor_order, shots_order)

    # If a valid selection was made, run the next steps
    if coffee_order:
        cost = calculate_cost(size_order)
        print_labels(first, last, coffee_order, size_order,
                     milk_order, flavor_order, shots_order, cost)
        # save_orders()  <-- Ready for next week


main()
