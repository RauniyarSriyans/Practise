# Given an array of strings strs, group the anagrams together. You can 
# return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters 
# exactly once.

def groupanagrams(strs):
    # Create a hashmap to store the sorted strings and their indices
    hashSet = {} # sorted string: index
    for i, s in enumerate(strs):
        # Sort the string
        sortedString = ''.join(sorted(s))
        # If the sorted string is in the hashmap, append the current 
        # index to the list of indices
        if sortedString in hashSet:
            hashSet[sortedString].append(i)
        # Else, add the sorted string to the hashmap
        else:
            hashSet[sortedString] = [i] # list of indices, so use []
    # Create a list to store the anagrams
    anagrams = []
    # Iterate through the hashmap and append the anagrams to the list
    for items in hashSet:
        anagram = []
        for i in hashSet[items]:
            anagram.append(strs[i])
        anagrams.append(anagram)
    return anagrams