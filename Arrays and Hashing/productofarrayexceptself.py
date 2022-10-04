# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums 
# except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in 
# a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using 
# the division operation.

def productExcceptSelf(nums):
    result = [] * len(nums) # create an empty list of length nums

    # First, add to result the product of all the elements to the left 
    # of the current element

    prodLeft = 1
    for i in range(len(nums)):
        result[i] = prodLeft
        prodLeft *= nums[i]

    # Second, add to result the product of all the elements to the right
    # of the current element
    
    prodRight = 1
    for i in range(len(nums)-1, -1, -1): # iterate backwards starting from
                                         # the last element in nums and go
                                         # until -1 (not inclusive); so, 
                                         # iterate from the last element to
                                         # the first element i.e. 0
        result[i] *= prodRight
        prodRight *= nums[i]
    
    return result
