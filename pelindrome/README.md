# Palindrome Checker

This is a simple Python program to check whether a given string is a palindrome.

## How It Works

The program:
1. Takes input from the user.
2. Checks if the input is the same when reversed.
3. Prints whether the input is a palindrome.

```python
# Function to check palindrome
def is_palindrome(word):
    return word == word[::-1]

# User input
text = input("Enter a string to check if it's a palindrome: ")

# Check and display result
if is_palindrome(text):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")