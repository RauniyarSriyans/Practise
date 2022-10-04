# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

# Example 1:
def containsDuplicate(nums):
    hashSet = set() # set cannot contain duplicates
    for item in nums:
        if item in hashSet:
            return True
        hashSet.add(item)
    return False

# Example 2:
def containsDuplicate2(nums):
    return len(nums) != len(set(nums))

# Example 1 is faster and more efficient than Example 2
