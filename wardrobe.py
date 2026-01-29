"""
conditionals - if then statements
"""

# # get a value
# temp = int(input("Whate is the outside temperataure (F)?  "))

# # is it cold???
# if temp <= 32:
#     print("It is Freezing!!!")

#     snow = input("Is it going to snow? (y/n)")
#     if snow == "y" or "Y":
#         print("Wear boots and a parka.")
#     else:
#         print("Don't forget your coat!")
# else:
#     print("It is warm enough for water")  # not freezing, roads may be wet
#     rain = input("Is it going to rain? (y/n)   ")
#     if rain == "y" or "Y":
#         print("Bring your umbrella")
#     else:
#         print("Sneakers are fine")


# elif

age = int(input("How old are you? "))
if age < 16:
    print("You can't drive yet.")
elif age < 18:
    print("You can't vote yet! ")
elif age < 21:
    print("You can't drink yet!")
elif age < 63:
    print("You can't retire yet!")
    print("Are you counting the years?")
else:
    print("Where would you like to retire to?")
