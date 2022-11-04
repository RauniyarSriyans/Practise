# Check whether two given words (or phrases) are anagrams or not

def isanagram(s, t):
    s = s.replace(" ", "")
    t = t.replace(" ", "")
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    if s_sorted == t_sorted:
        return True 
    return False 

if __name__ == '__main__':
    s = 'rest ful'
    t = 'flu ster'
    print(isanagram(s, t))