# Reversing an array in place in O(n) time and O(1) space

def reverse(arr):
    start = 0
    end = len(arr) - 1 
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1 
    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    print(reverse(arr))

