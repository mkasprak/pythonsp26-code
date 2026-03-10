"""
📚 ADD-100: Intro to Python | Demo: Resilient Lookup Schema
"""

# 1. Define the Schema
translator = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco"
}

word = input("Enter an English number (one-five): ").lower().strip()

# 2. Perform a Resilient Lookup
try:
    translation = translator[word]
    print(f"System Output: {translation}")
except KeyError:
    print(f"!! DATA INTEGRITY WARNING: '{word}' is not in our system.")