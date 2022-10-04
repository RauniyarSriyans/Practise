# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original
# list of strings.

# Please implement encode and decode 

def encode(strs):
    # encode the list of strings into a single string using the following
    # format: <length of string>#<string> and so on
    encStr = ''
    for s in strs:
        encStr += str(len(s)) + '#' + s
    return encStr

def decode(s):
    decStr = []
    # i is the index of the string
    i = 0
    while i <len(s):
        # j is the index to find the length of the string and the string
        j = i
        # find the index to the last character of the length of the string
        while s[j] != '#':
            j += 1
        # get the length 
        length = int(s[i:j])
        # get the string of the length and append the string to decStr
        decStr.append(s[j+1:j+1+length])
        i = j+1+length
    return decStr

def main():
    encode(["Hello", "World"])
    decode("Hello World")