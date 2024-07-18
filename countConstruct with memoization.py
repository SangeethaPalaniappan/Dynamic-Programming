# countConstruct with memoization

def canConstruct(string, arr, hashmap):
    if string in hashmap:
        return hashmap[string]
    if len(string) == 0:
        return 1
    cnt = 0
    for i in range(len(arr)):
        char = len(arr[i])
        if arr[i] == string[0:char]:
            res = canConstruct(string[char:len(string)], arr, hashmap)
            hashmap[string] = cnt
            cnt += res
                
    hashmap[string] = cnt
    return cnt
    

call1 = canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {})
print("count", call1)
call2 = canConstruct("skateboard",["ate", "rd", "boar", "bo", "sk", "ska"], {})
print("count", call2)
call3 = canConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"], {})
print("count", call3)
call4 = canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eeee", "eeeeee", "e", "eeee"], {})
print(call1, call2)
print(call3, call4)
call5 = canConstruct("purple", [ "pur", "p", "le", "purp", "eeee"], {})
print(call5)
