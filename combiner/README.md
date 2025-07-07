# Text Combiner & Iterator

This is a simple Python program that takes two text inputs, combines them, and returns a list of all characters from the combined string.

---

## What It Does

1. Takes two inputs from the user.
2. Combines them into a single string.
3. Converts the combined string into a list of characters.
4. Displays the result to the user.

---

## Example

**Input:**


## code example

# Function to combine and iterate
def combine_and_iterate(text1, text2):
    combined = text1 + text2
    characters = list(combined)
    return characters

# User input
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

# Process and print
result = combine_and_iterate(text1, text2)
print("Combined characters:", result)
print("Thank you for using my application")
