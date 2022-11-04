# Check whether a string is pallindrome or not

# Method 1: Using O(n) time and traversing 
def pallindrome1(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

# Method 2: Using slicing 
def pallindrome2(string):
    return string == string[::-1]

if __name__ == '__main__':
    string = 'racecar'
    print(pallindrome1(string))
    print(pallindrome2(string))
