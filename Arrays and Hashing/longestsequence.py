# Given an unsorted array of integers nums, return the length of the 
# longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longestSequence(nums):
    # Create a set of the elements in nums
    numSet = set(nums)
    # Initialize the longest sequence to 0
    longest = 0
    # Iterate through the set
    for num in numSet:
        # If num-1 is not in the set, then num is the first element of a 
        # sequence
        if (num-1) not in numSet:
            # Initialize the current sequence to 1
            len = 1
            # While the next number in the sequence is in the set, increment
            # the current sequence and the current number
            while (num+len) in numSet:
                len += 1
            # Update the longest sequence
            longest = max(longest, len)
    return longest
