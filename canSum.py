# CanSum with tabulation

def fun(tot, target, arr, res, hashmap):
    if tot in hashmap:
        return hashmap[tot]
    if tot == target:
        return 1
    if tot > target:
        return 0
    res = 0
    for i in range(len(arr)):
        res = fun(tot + arr[i], target, arr, res, hashmap)
        hashmap[tot + arr[i]] = res
        if res == 1:
            return 1
    return res
ans = fun(0, 300, [7,14], 0, {})
print(ans)
print(fun(0, 7, [2, 4], 0, {})) # false
print(fun(0, 7, [2, 3], 0, {})) # true
print(fun(0, 8, [2, 3, 5, 4], 0, {})) # true
print(fun(0, 300, [7, 14], 0, {})) # false
