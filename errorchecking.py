"""
Input validation

"""

# Rent a car
first_name = ""
while len(first_name) == 0:

    first_name = input("What is your legal First name? ")

last_name = ""
while len(last_name) == 0:
    last_name = input("What is your legal last name? ")

age = 0
while age < 16:
    age = int(input("What is your age? "))
    if age < 0 or age > 70:
        print("I'm sorry, that is not a valid age")
    elif age > 24:
        pass
    else:
        print("I'm sorry, we cannot rent to you")

valid = input("Do you have a valid drivers license (Y/N)").upper()

if valid == "Y":
    print("What kind of car would you like to rent")
else:
    print("I'm Sorry, we cannot rent to you")
