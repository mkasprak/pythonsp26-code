"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Quacken Coffee POS (V3.0)
Developer: Monty PyDuck
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")


def get_customer_info():
    """Asks for name and office location."""
    name = input("Customer Name: ").title()
    location = input("Office Number: ")
    return name, location


def take_order():
    """Collects choices. Notice the tuple usage for milk options."""
    cat = input("Drink Category (Coffee/Tea/Cocoa): ")
    size = input("Size (Small/Medium/Large): ")
    print(f"Available Milk: {MILK_OPTIONS}")
    milk = input("Choice of milk: ")
    pumps = int(input("How many pumps? "))
    return {"category": cat, "size": size, "milk": milk, "pumps": pumps}


def calculate_total(order_data):
    """Calculates price based on size and pumps."""
    base_price = 4.00
    syrup_cost = order_data["pumps"] * 0.10
    return base_price + syrup_cost


def save_data_and_label(customer, location, total):
    """Appends to order_history.txt and prints the human-readable label."""
    print(f"--- BARISTA TICKET ---")
    print(f"ROOM: {location} | ATTN: {customer}")
    print(f"TOTAL: ${total:.2f}")


def main():
    # 1. Identity Phase
    name, location = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase (Using KEYWORD ARGUMENTS)
    save_data_and_label(customer=name, location=location, total=final_price)


main()
