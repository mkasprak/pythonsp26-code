"""
some while loops
"""

keep_going = True
while keep_going:
    print("This is the song that never ends. \n It just goes on and on my friend")
    print("Somebody started singing it not knowing what it was")
    print("And they'll just go on singing it forever just because.")

    somebody_stop_me = input("Keep going? y/n:   ")
    if somebody_stop_me == "y" or somebody_stop_me == "Y":
        keep_going = True
    else:
        keep_going = False


# for loop
# range(start, stop, step)
# This starts at 10, stops BEFORE it hits 0, and steps by -1
for i in range(10, 0, -1):
    print(f"{i}...")

print("🚀 BLAST OFF!")
print("      !")
print("     / \\")
print("    |   |")
print("    |   |")
print("   /|   |\\")
print("  /_|___|_\\")
print("    m m m")


for day in ("Sunday", "Monday", "Tuesday", "Wednesday"):
    print(day)
