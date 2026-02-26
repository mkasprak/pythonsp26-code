"""
in demo
"""

my_string = "Meri Kasprak"
if "Dr." in my_string:
    print("Yes, individual has a doctorate")
else:
    print("no, does not have a doctorate")


days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

for day in days:
    if day.startswith("S"):
        print(day)
