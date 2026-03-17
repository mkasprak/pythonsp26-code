"""Demonstrate functions in our coffee order"""

# GLOBAL CONSTANTS (Pantry Rules - Visible to all)
MILK_TYPES = ("Oat", "Almond", "2%")


def brew_custom(customer, milk="2%", sugar=0):
    """Processes inbound data and local logic."""
    print(f"\n--- OFFICIAL TICKET: {customer.upper()} ---")
    print(f"Recipe: Coffee with {milk} milk and {sugar} sugars.")


def main():

    try:
        user = input("Duck Name: ").title()
        print(f"Options: {MILK_TYPES}")  # Accessing Global Scope
        choice = input("Select Milk: ").title()
        pumps = int(input("Sugars? (as a number 1, 2, 3, etc.)"))
    except ValueError:
        print("Invalid input. Defaulting to 0.")
        pumps = 0

    # Keyword Handoff
    brew_custom(customer=user, milk=choice, sugar=pumps)


main()
# Done, we are moving to lab time.
