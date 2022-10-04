# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters 
# exactly once.

# Example 1: Uses a hashmap to count the number of times a letter appears
# This method uses extra space to store the hashmap, so not O(1) space
def anagram(s, t):
    if len(s) != len(t):
            return False
        
    sSet, tSet = {}, {}
        
    for i in range(len(s)):
        # Here, the get method gets the key's value if it exists, else
        # returns 0; doesn't throw an error that the key doesn't exist
        sSet[s[i]] = 1 + sSet.get(s[i], 0)
        tSet[t[i]] = 1 + tSet.get(t[i], 0)
        
    for items in sSet:
        if sSet[items] != tSet.get(items, 0):
            return False
        
    return True

# Example 2: Uses a cheat method called Counter
import collections
def anagram2(s, t):
    return collections.Counter(s) == collections.Counter(t)

# Example 3: Uses a sorting method to compare the two strings; is O(nlogn)
# in average case, but O(n^2) in worst case; but is O(1) space
def anagram3(s, t):
    return sorted(s) == sorted(t)

   