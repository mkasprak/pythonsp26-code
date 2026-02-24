# 1. SETUP: Strings are immutable, so we use a list
name_string = "BINGO"
dog_letters = list(name_string)
count = 0

# 2. THE LOOP: This runs once for each character in "BINGO"
for char in name_string:
    # STRING METHOD: .join() combines items into one string
    current_name = " ".join(dog_letters)

    print("There was a farmer who had a dog and Bingo was his Name-o")
    print(f"({current_name}) \n" * 3)  # String replication * 3
    print("and Bingo was his Name-o!\n")

    # Replace the letter at our current index with a dog face
    dog_letters[count] = "🐩"
    count += 1

# 3. THE FINALE: The loop is over, but we show the final version!
final_name = " ".join(dog_letters)
print(f"({final_name}) \n" * 3)
print("and Bingo was his Name-o!")
