# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    sol = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue
        
        leftPointer = i + 1
        rightPointer = len(nums) - 1

        while leftPointer < rightPointer:
            threesum = n + nums[leftPointer] + nums[rightPointer]
            if threesum < 0:
                leftPointer += 1
            elif threesum > 0:
                rightPointer -= 1
            else:
                sol.append([n, nums[leftPointer], nums[rightPointer]])
                leftPointer += 1
                while n == nums[leftPointer] and leftPointer < rightPointer:
                    leftPointer += 1
    return sol
