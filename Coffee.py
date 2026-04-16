"""
    creating the coffee class
"""


class Coffee:
    def __init__(self, coffee_type, size, milk, flavor, pumps):
        # Private attributes
        self.__coffee_type = coffee_type
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__pumps = pumps

    # --- Getters ---
    def get_coffee_type(self):
        return self.__coffee_type

    def get_size(self):
        return self.__size

    def get_milk(self):
        return self.__milk

    def get_flavor(self):
        return self.__flavor

    def get_pumps(self):
        return self.__pumps

    # --- Setters ---
    def set_coffee_type(self, coffee_type):
        self.__coffee_type = coffee_type

    def set_size(self, size):
        self.__size = size

    def set_milk(self, milk):
        self.__milk = milk

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def set_pumps(self, pumps):
        self.__pumps = pumps

    # --- Summary Output ---
    def get_summary(self):
        return (f"Order Summary: {self.__size} {self.__coffee_type} "
                f"with {self.__milk} milk, {self.__flavor} flavor, "
                f"and {self.__pumps} pumps.")


coffee1 = Coffee("Latte", "Large", "Whole", "Vanilla", 3)
coffee2 = Coffee("Matcha", "Medium", "Coconut", "none", 0)


print(coffee1.get_summary())
print(coffee2.get_summary())