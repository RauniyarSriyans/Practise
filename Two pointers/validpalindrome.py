# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters 
# include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1: Takes extra space and uses in built library (isalnum)

def isPalindrome(s):
    # Define a new string that contains only alphanumeric characters
    newStr - ""
    # Go through each character in s
    for char in s:
        # Check if the character is alphanumeric
        if char.isalnum():
            # If it is, add it to the new string
            newStr += char
    # Convert the new string to lowercase
    newStr = newStr.lower()
    # Check and return if the reversed new string is equal to the string
    return newStr == newStr[::-1]

# Example 2: Uses two pointers

# helper function to check if a character is alphanumeric
def alphaNumeric(char):
    # ord returns the unicode code point for a one-character string
    return ((ord('A') <= ord(char) <= ord('Z')) 
        or (ord('a') <= ord(char) <= ord('z')) 
        or (ord('0') <= ord(char) <= ord('9')))

# checker function
def isPalindrome(s):
    leftPointer = 0
    rightPointer = len(s) - 1

    while leftPointer < rightPointer:
        while leftPointer < rightPointer and not alphaNumeric(s[leftPointer]):
            leftPointer += 1
        while leftPointer < rightPointer and not alphaNumeric(s[rightPointer]):
            leftPointer += 1
        if s[leftPointer] != s[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1
    return True


