# GLOBAL CONSTANTS
TAX_RATE = 0.05


def calculate_result(base_price, item_desc):
    """Calculates tax and returns TWO values (total, status)."""
    tax = base_price * TAX_RATE
    total = base_price + tax
    item_desc = item_desc.title()

    return total, item_desc


def main():
    try:
        item = input("Enter item name: ")
        user_price = float(input("Enter order price: "))
    except ValueError:
        print("Invalid input. Defaulting to 1.00")
        user_price = 1.00
        item = "unknown"
    except Exception as e:
        print(e)

    # UNPACKING the two returned values
    final_cost, item_txt = calculate_result(
        base_price=user_price, item_desc=item)

    print(f"\nFinal Receipt: ${final_cost:.2f}")
    print(f"Order: {item_txt}")


main()
