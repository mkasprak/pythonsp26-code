"""
conditional logic
"""

a = 10
b = 20
c = -10

print("\n\n\n\n")
print(a > c)
print(a > c and c > b)
print(a > c or c > b)

print("c > 0: ", (c > 0))

print("c != 0: ", (c != 0))


grade = int(input("What was your score on the test? "))

if grade > 90:
    letter_grade = "A"
elif grade > 80:
    letter_grade = "B"
elif grade > 70:
    letter_grade = "C"
elif grade > 60:
    letter_grade = "D"
else:
    grade = "F"


print(f"Your grade is {letter_grade}")
