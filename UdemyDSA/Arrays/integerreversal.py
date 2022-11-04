# Reverse an integer 

def reverse_integer(num):
    rem = 0
    ret = 0
    while num > 0:
        rem = num % 10 
        ret = ret * 10 + rem 
        num = num // 10
    return ret
    
if __name__ == '__main__':
    num = 1234
    num = reverse_integer(num)
    print(num)