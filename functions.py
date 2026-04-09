"""
    Demonstrate functions
"""


def options():
    # give options to order, print labels, see history
    pass


def read_orders():
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
    print("Save Orders")

    print("Print labels")


def calculate_cost():
    # Calculate cost (read in order)
    print("Calculate cost")


def print_labels():
    pass


def main():
    options()
    order_system()
    calculate_cost()
    print_labels()


main()
