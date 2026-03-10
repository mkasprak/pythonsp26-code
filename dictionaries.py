"""
    working with dictionaries
    
"""

# create dictionary
japanese_numbers = {
    "one": "ichi",
    "two": "ni",
    "three": "san",
    "four": "yon",
    "five": "go",
    "six": "roku",
    "seven": "nana",
    "eight": "hachi",
    "nine": "kyuu",
    "ten": "juu"
}


if "eleven" in japanese_numbers:
    print("found")
else:
    print("missing")
    
#lookup by key
print(japanese_numbers["seven"])

# days in months

days_in_months = {
    "January": 30,
    "Febuary": 28,
    "March":31
}

for key, value in days_in_months.items():
    print(f"{key}:{value}")
print("\n\n")
    
    
days_in_months["April"] = 30

for key, value in days_in_months.items():
    print(f"{key}:{value}")
print("\n\n")

# delete
days_in_months. pop("January")
for key, value in days_in_months.items():
    print(f"{key}:{value}")
print("\n\n")