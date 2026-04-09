
# This script demonstrates a coffee ordering system with menu reading,
# user input, and file writing.
# It is thoroughly annotated to help students understand each part of the code.
"""
    Write to files
"""

"""
1. Demonstrate functions
2. Interface design (menus/ passing)
"""


# This function collects employee identification details from the user.
def lookup():
    """Collects employee identification details."""
    fname = input("Please Enter First Name: ")  # Prompt for first name
    lname = input("Please Enter your Last Name: ")  # Prompt for last name
    extension = input("Please enter your extension: ")  # Prompt for extension
    # Prompt for employee number
    emp_num = input("Please enter your employee number: ")

    # Return all collected details as a tuple
    return fname, lname, extension, emp_num


# This function reads the menu from 'menu.txt' and stores it in a dictionary.
def read_menu():
    """ read_menu will import menu.txt and pull it into a list. We can then
        break down the list into the specific variables and
        dictionaries that we need. """
    menus = {}
    try:
        # open and read file
        with open("menu.txt", 'r') as file:
            for line in file:
                # Each line is split into category and detail using ';'
                parts_of_line = line.strip().split(';')
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

        # Uncomment to print all menu items for debugging
        # for x, y in menus.items():
        #     print(x, y)
        return menus
    except Exception as e:
        # Print any error that occurs (e.g., file not found)
        print(e)


# This function splits the menu dictionary into separate variables
# for each menu section.
def split_into_variables(menu_items):
    """break the menu file into separate variables"""
    print("In split_into_variables")  # Debug print

    # Extract each menu section by key
    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")

    # Return all menu sections as a tuple
    return coffee, prices, milks, flavors, shots


# This function displays the menu options and captures all user
# selections for the drink.
def ordering_system(coffee_menu, prices_menu, milks_menu,
                    flavors_menu, shots_menu):
    """Displays menus and captures all user selections for the drink."""

    # Test print to show function is running
    print("Test ordering system")
    # Print all menu sections for debugging
    print(f"drinks: {coffee_menu}\nprices: {prices_menu}\nmilks:{milks_menu}")
    print(f"flavors: {flavors_menu}\nshots: {shots_menu}")
    try:
        # TODO - change input to right after each menu displays
        nbr = 1
        # 1. Display coffee Types
        print("\n--- DRINK TYPES ---")
        coffee_item = coffee_menu.split(',')  # Split coffee menu into items
        for item in coffee_item:
            item = item.strip()
            print(f"\t{nbr}.  {item}")  # Print each coffee option
            nbr += 1
        drink_idx = int(input("Select Drink Number: ")) - \
            1  # User selects drink

        # 2. Display Sizes and prices
        print("\n--- SIZES ---")
        # Using a list to allow numeric selection from the dictionary
        print(prices_menu)  # Debug print
        nbr = 1
        size_item = prices_menu.split(',')  # Split sizes
        # The following loop is a placeholder; actual price lookup may differ
        for size in size_item:
            size = size.strip()
            print(f"\t{nbr}. {size}")
            nbr += 1
        size_idx = int(input("Select Size Number: ")) - 1  # User selects size

        # 3. Display Milk Options
        print("\n--- MILK OPTIONS ---")
        nbr = 1
        milk_item = milks_menu.split(',')  # Split milks
        for milk in milk_item:
            milk = milk.strip()
            print(f"\t{nbr}. {milk}")
            nbr += 1
        milk_idx = int(input("Select Milk Number: ")) - 1  # User selects milk

        # 4. Display Flavor Options
        print("\n--- FLAVOR ADD-INS ---")
        nbr = 1
        flavor_item = flavors_menu.split(',')  # Split flavors
        for flavor in flavor_item:
            flavor = flavor.strip()
            print(f"\t{nbr}. {flavor}")
            nbr += 1
        flavor_idx = int(input("Select Flavor Number: ")) - \
            1  # User selects flavor

        # 5. Display Shot Strength
        print("\n--- SHOT STRENGTH ---")
        nbr = 1
        shot_item = shots_menu.split(",")  # Split shots
        for shot in shot_item:
            shot = shot.strip()
            print(f"{nbr}. {shot}")
            nbr += 1
        shot_idx = int(input("Select Shot Strength: ")) - \
            1  # User selects shot

        # Map indices back to names for confirmation
        # Note: These are string splits, not lists,
        # so we split again for lookup
        drink = coffee_item[drink_idx]
        size = size_item[size_idx]
        milk = milk_item[milk_idx]
        flavor = flavor_item[flavor_idx]
        shot = shot_item[shot_idx]

        # Print the user's full order for confirmation
        print(
            f"\n{size} {drink} with {milk} milk, shots {shot} of {flavor}")

        return drink, size, milk, flavor, shot

    except Exception as e:
        # Catch any input or index errors and inform the user
        print(f"Input Error: {e}")
        return None, None, None, None, None


# Placeholder for next week: Read file to display last 5 unique orders
def read_orders():
    pass


# This function saves the order details to 'orders.txt'.
def save_orders(first, last, ext, coffee, size, milk, flavor, shots):
    with open("orders.txt", "a") as file:
        file.write(
            f"{first}, {last}, {coffee}, {size}, {milk}, {flavor}, {shots}\n")


# This function prints a label for the order.
def print_labels(first, last, coffee, size, milk, flavor, shots, cost):
    print(f"{first} {last}\nDrink: {coffee}\nSize: {size}\nMilk Type:{milk}")
    print(f"Flavor: {flavor}, Number of pumps: {shots}")


# This function calculates the cost based on the selected size.
def calculate_cost(size_name, prices_menu):
    """Calculates total based on the selected size key."""
    # This is a placeholder; actual price lookup may differ
    # if size_name in prices_menu:
    #     cost = prices_menu[size_name]
    #     print(f"Total Cost for paycheck deduction: ${cost:.2f}")
    #     return cost
    # else:
    #     print("Cost calculation unavailable.")
    #     return 0


# Main function to run the program
def main():
    # User Lookup: get employee info
    first, last, ext, emp = lookup()

    # Read in external menu file
    menu_items = read_menu()

    # Split menu into variables for each section
    coffee_menu, prices_menu, milks_menu, flavors_menu, shots_menu = \
        split_into_variables(menu_items)

    # Run Ordering Menu: get all user selections
    coffee_order, size_order, milk_order, flavor_order, shots_order = \
        ordering_system(coffee_menu, prices_menu, milks_menu,
                        flavors_menu, shots_menu)
    # Save the order to file
    save_orders(first, last, ext, coffee_order, size_order,
                milk_order, flavor_order, shots_order)

    # If a valid selection was made, run the next steps
    if coffee_order:
        cost = calculate_cost(size_order, prices_menu)
        print_labels(first, last, coffee_order, size_order,
                     milk_order, flavor_order, shots_order, cost)
        # save_orders()  <-- Ready for next week


# Run the main function if this script is executed
main()
