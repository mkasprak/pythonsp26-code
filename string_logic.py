"""
String Logic
"""

# Testing data
errors = True
while errors:
    try:
        name = input("Please enter your First and last name: ").title()
        first_name, last_name = name.split(" ")
        print(name)
        print(first_name)
        print(last_name)
        print(f"{first_name[0]}{last_name[0]}")
        errors = False
    except ValueError as e:
        print(f"You have a vaule error: {e}")

    except Exception as e:
        print(f"This raised an exception: {e}")
