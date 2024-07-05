# CanSum
from datetime import datetime
arr = [2,4]
targetSum = 7
def recursive(arr, n, hashmap):
    if n in hashmap:
        return hashmap[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    for i in arr:
        #print(i)
        n = n - i
        #print(n)
        res = recursive(arr, n, hashmap)
        if n not in hashmap:
            hashmap[n] = res
        if res == 1:
            return res
    return 0
start = datetime.now()          
print(recursive([2, 4], 7, {}))
print(recursive([2, 3], 7, {}))
print(recursive([2, 3, 5, 4], 8, {}))
print(recursive([7, 14], 300, {}))
end = datetime.now()          
print(end - start)    
