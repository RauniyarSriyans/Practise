# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and 
# you may not use the same element twice.

# You can return the answer in any order.

def twosum(nums, target):
    # Create a hashmap to store the values and their indices
    hashSet = {} # value: index
    for i, n in enumerate(nums):
        # If the target minus the current number is in the hashmap, 
        # return the current index and the index of the target minus 
        # the current number
        diff = target - n
        if diff in hashSet:
            return [i, hashSet[diff]]
        # Else, add the current number to the hashmap
        hashSet[n] = i



        