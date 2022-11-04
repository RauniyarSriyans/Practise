# Given a one-dimensional array of integers 0, 1, and 2 (3 different values), 
# sort this in linear time using constant memory 

def dutchflag(arr): 
    pivot = 1
    i,j = 0, 0
    k = len(arr) - 1 
    while j <= k:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1 
            j += 1
        elif arr[j] > pivot:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1 
    return arr


if __name__ == '__main__':
    arr = [1,1,2,2,2,1,0,0,1,1,2,0,0]
    print(dutchflag(arr))