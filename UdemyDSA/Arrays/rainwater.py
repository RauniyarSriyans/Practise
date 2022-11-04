# Given n non-negative integers representing an elevation map where the 
# width of each bar is 1. Compute how much water it can trap after raining!

def rainwater(height_arr):
    length = len(height_arr)
    trapped = [0 for i in range(length)]

    right_max = [0 for i in range(length)]
    left_max = [0 for i in range(length)]
   
    for i in range(1, length - 1, 1):
        left_max[i] = max(left_max[i-1], height_arr[i-1])
    
    for i in range(length - 2, -1, -1):
        right_max[i] = max(right_max[i+1], height_arr[i+1])

    for i in range(1, length - 1):
        if(min(right_max[i], left_max[i]) > height_arr[i]):
            trapped[i] = min(right_max[i], left_max[i]) - height_arr[i]

    return sum(trapped)

     
if __name__ == '__main__':
    arr = [1, 0, 2, 1, 3, 1, 2, 0, 3]
    print(rainwater(arr))