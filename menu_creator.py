"""
    Writing to files
    Date/time
    Create Menu text file for Coffee house
"""


def get_menu_options():
    # get info for menu dictionary
    menu = {}
    while True:
        print("Type 'Q' when done")
        category = input(
            "Please give me the category for this part of the menu: ").upper()
        if category == "Q":
            break
        items = input("Please enter items separated by commas: ")

        # add to dictionary
        menu[category] = items

    return menu


def save_to_file(menu):

    # Open the log file in append mode ('a') so new entries are appended
    with open("menu.txt", "a") as file:
        all_items = menu.items()
        print(all_items)
        for item in all_items:
            output = (f"{item[0]} ; {item[1]}")
            print(output)
            file.write(output + "\n")


def main():
    my_menu = get_menu_options()
    save_to_file(my_menu)
    # Print confirmation to the user


# Run the main function if this script is executed
main()
