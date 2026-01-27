"""
    Demo using and formatting numbers
"""

# convert input

allowence = float(input("How much is your allowence?  "))
snacks = float(input("Amount spent on snacks?  "))
video_games = float(input("Spent on video games?  "))


# Equation
spent = snacks + video_games
remaining = allowence - snacks - video_games
percent = snacks/allowence

# Display

print(f"You recieve {allowence: ,.2f}")
print(f"You spend {spent: ,.2f} a month.")
print(f"You have {remaining: ,.2f} left")
print(f"You spent %{percent:.2f} on snacks.")