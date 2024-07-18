# allConstruct with memoization


def canConstruct(string, arr, hashmap):
    if string in hashmap:
        return hashmap[string]
    if string == "":
        return [[]]
    f_arr = []
    for i in range(len(arr)):
        char = len(arr[i])
        if arr[i] == string[0:char]:
            res = canConstruct(string[char:len(string)], arr, hashmap)
            if len(res) != 0:   
                for k in res:
                    k.insert(0, arr[i]) 
                f_arr = f_arr + res
            hashmap[string] = f_arr
            
                
    hashmap[string] = f_arr
    return f_arr
    

call1 = canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {})
print("count", call1)
call2 = canConstruct("skateboard",["ate", "rd", "board", "bo", "sk", "ska"], {})
print("count", call2)
call3 = canConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"], {})
print("count", call3)
call5 = canConstruct("purple", [ "ur", "p", "le", "purp", "purpl"], {})
print(call5)
call4 = canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eeee", "eeeeee", "e", "eeee"], {})
print(call1, call2)
print(call3, call4)
