"""

    test reading in our menu and creating lists and dictionaries

"""


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

    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")

    return coffee, prices, milks, flavors, shots


def print_menu(coffee, prices, milks, flavors, shots):
    """Will print each menu"""
    print("Coffee\n")
    coffee_item = coffee.split(',')
    for item in coffee_item:
        item = item.strip()
        print(f"\t{item}")


def main():
    """organize program logic"""
    menu_items = read_menu()
    coffee, prices, milks, flavors, shots = split_into_variables(menu_items)
    print_menu(coffee, prices, milks, flavors, shots)


main()
