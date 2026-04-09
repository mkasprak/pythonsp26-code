
"""
    This script demonstrates a coffee ordering system with menu reading,
    user input, and file writing.
    It is thoroughly annotated to help students understand each
    part of the code.
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
    pumps = menu_items.get("PUMPS")

    # Return all menu sections as a tuple
    return coffee, prices, milks, flavors, pumps


# This function displays the menu options and captures all user
# selections for the drink.
def ordering_system(coffee_menu, prices_menu, milks_menu,
                    flavors_menu, pumps_menu):
    """Displays menus and captures all user selections for the drink."""

    # Test print to show function is running
    print("Test ordering system")
    # Print all menu sections for debugging
    print(f"drinks: {coffee_menu}\nprices: {prices_menu}\nmilks:{milks_menu}")
    print(f"flavors: {flavors_menu}\npumps: {pumps_menu}")
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

        # 5. Display Pumps of Flavor
        print("\n--- PUMPS OF FLAVOR ---")
        nbr = 1
        pumps_item = pumps_menu.split(",")  # Split pumps
        for pumps in pumps_item:
            pumps = pumps.strip()
            print(f"{nbr}. {pumps}")
            nbr += 1
        pumps_idx = int(input("Select number of pumps: ")) - \
            1  # User selects pumps

        # Map indices back to names for confirmation
        drink = coffee_item[drink_idx]
        size = size_item[size_idx]
        milk = milk_item[milk_idx]
        flavor = flavor_item[flavor_idx]
        pumps = pumps_item[pumps_idx]

        # Print the user's full order for confirmation
        print(
            f"\n{size} {drink} with {milk} milk, {pumps} pumps of {flavor}")

        return drink, size, milk, flavor, pumps

    except Exception as e:
        # Catch any input or index errors and inform the user
        print(f"Input Error: {e}")
        return None, None, None, None, None


# print each unique order for the current emp_num
def read_orders(emp_num):
    try:
        with open("orders.txt", "r") as file:
            lines = file.readlines()

        unique_orders = []
        for line in lines:
            parts = line.split(",")
            if len(parts) < 4:
                continue
            if parts[3].strip() == emp_num:
                if line not in unique_orders:
                    unique_orders.append(line)
                    print(line.strip())
        if not unique_orders:
            print("No orders found for this employee number.")
    except FileNotFoundError:
        print("No orders found. The file 'orders.txt' does not exist yet.")
    except Exception as e:
        print(f"An error occurred: {e}")


# This function saves the order details to 'orders.txt'.
def save_orders(first, last, ext, emp, coffee, size, milk, flavor, shots):
    with open("orders.txt", "a") as file:
        file.write(
            f"{first}, {last}, {ext}, {emp}, {coffee}, {size}, \
                {milk}, {flavor}, {shots}\n")


# This function prints a label for the order.
def print_labels(first, last, coffee, size, milk, flavor, shots, cost):
    print(f"{first} {last}\nDrink: {coffee}\nSize: {size}\nMilk Type:{milk}")
    print(f"Flavor: {flavor}, Number of pumps: {shots}")


# This function calculates the cost based on the selected size.
def calculate_cost(size_name, prices_menu):
    """Calculates total based on the selected size key."""
    # Assume prices_menu is a comma-separated string like
    # 'Small:2.00,Medium:2.50,Large:3.00'
    prices = {}
    for item in prices_menu.split(","):
        if ":" in item:
            size, price = item.split(":")
            prices[size.strip()] = float(price.strip())
    if size_name in prices:
        cost = prices[size_name]
        print(f"Total Cost for paycheck deduction: ${cost:.2f}")
        return cost
    else:
        print("Cost calculation unavailable.")
        return 0


# Main function to run the program
def main():
    # User Lookup: get employee info
    first, last, ext, emp = lookup()

    # Read in external menu file
    menu_items = read_menu()

    # Split menu into variables for each section
    coffee_menu, prices_menu, milks_menu, flavors_menu, pumps_menu = \
        split_into_variables(menu_items)

    # Run Ordering Menu: get all user selections
    coffee_order, size_order, milk_order, flavor_order, pumps_order = \
        ordering_system(coffee_menu, prices_menu, milks_menu,
                        flavors_menu, pumps_menu)

    # Save the order to file
    save_orders(first, last, ext, emp, coffee_order, size_order,
                milk_order, flavor_order, pumps_order)

    # Print the order for review
    print("\nYour order has been saved. Here is your order:")
    print_labels(first, last, coffee_order, size_order,
                 milk_order, flavor_order, pumps_order, 0)

    # Ask the user if they want to change, cancel, or proceed
    print("\nWould you like to:")
    print("1. Change your order")
    print("2. Cancel (delete) your order")
    print("3. Proceed (keep order as is)")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print("\nLet's change your order. Please re-enter your selections.")
        # Re-run the ordering system and overwrite the last order
        coffee_order, size_order, milk_order, flavor_order, pumps_order = \
            ordering_system(coffee_menu, prices_menu, milks_menu,
                            flavors_menu, pumps_menu)
        # Overwrite the last order (delete and re-save)
        update_last_order(emp, first, last, ext, coffee_order,
                          size_order, milk_order, flavor_order, pumps_order)
        print("Order updated!")
        print_labels(first, last, coffee_order, size_order,
                     milk_order, flavor_order, pumps_order, 0)
    elif choice == "2":
        print("\nYour order will be deleted.")
        delete_last_order(emp)
        print("Order deleted.")
    else:
        print("Order kept as is.")

    # If a valid selection was made, run the next steps
    if coffee_order:
        cost = calculate_cost(size_order, prices_menu)
        print_labels(first, last, coffee_order, size_order,
                        milk_order, flavor_order, pumps_order, cost)

    # Helper function to update the last order for the current employee

    def update_last_order(emp_num, first, last, ext, coffee, size, milk, flavor, pumps):
        try:
            with open("orders.txt", "r") as file:
                lines = file.readlines()
            # Find the last order for this employee
            for i in range(len(lines) - 1, -1, -1):
                parts = lines[i].split(",")
                if len(parts) > 3 and parts[3].strip() == emp_num:
                    # Replace this line with the new order
                    lines[i] = f"{first}, {last}, {ext}, {emp_num}, {coffee}, {size}, {milk}, {flavor}, {pumps}\n"
                    break
            with open("orders.txt", "w") as file:
                file.writelines(lines)
        except Exception as e:
            print(f"Error updating order: {e}")

    # Helper function to delete the last order for the current employee
    def delete_last_order(emp_num):
        try:
            with open("orders.txt", "r") as file:
                lines = file.readlines()
            # Find and remove the last order for this employee
            for i in range(len(lines) - 1, -1, -1):
                parts = lines[i].split(",")
                if len(parts) > 3 and parts[3].strip() == emp_num:
                    del lines[i]
                    break
            with open("orders.txt", "w") as file:
                file.writelines(lines)
        except Exception as e:
            print(f"Error deleting order: {e}")


# Run the main function if this script is executed
main()
