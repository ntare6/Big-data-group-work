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