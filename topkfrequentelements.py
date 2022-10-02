# Given an integer array nums and an integer k, return the k most 
# frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
    # Number: Frequency
    count = {}
    track = [[] for i in range(len(nums) + 1)] #Stores the number in the
    # respective index according to its frequency
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Store the numbers in the respective index according to its frequency
    for key, value in count.items():
        track[value].append(key)

    res = []

    for i in range((len(track) - 1), 0, -1):
        for n in track[i]:
            res.append(n)
            if len(res) == k:
                return res
