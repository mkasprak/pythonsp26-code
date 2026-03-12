"""
Functions demo
"""


def print_days(days):
    for day in days:
        print(day)


def greeting(name, birth_year):
    # pass  - DNGN( Star trek Does nothing, goes nowhere)
    print(f"Hello, {name}")
    year = 2026
    age = year - birth_year
    print(f"Hello, {name}. You are {age} years old.")
    return name, age


def main():
    # organizes and calls functions from here!
    person = input("What is your name? ")
    year = int(input("What year were you born:  "))
    p2, age = greeting(person, year)
    days = (
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    )
    print_days(days)


main()
