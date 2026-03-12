"""
Demonstrate functions
"""


def options():
    # give options to order, print labels, see history
    pass


def menu():
    # present menu options
    print("Menu")


def order_system():
    print("Order System")
    # take orders from customer
    # read in past orders and display
    # call save function
    menu()

    # name = input("Please enter your name: " )
    # read file to look for last order

    read_orders()

    save_orders()


def read_orders():
    # reads stored orders
    pass


def save_orders():
    # Write to file
    print("Save Orders")


def print_labels():
    # print on avery 2 by 3 inch labels
    print("Print labels")


def calculate_cost():
    # Calculate cost (read in order)
    print("Calculate cost")


def main():
    options()
    order_system()
    calculate_cost()
    print_labels()


main()
