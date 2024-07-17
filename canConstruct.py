# canConstruct

def canConstruct(string, arr):
    if len(string) == 0:
        return 1
    for i in range(len(arr)):
        char = len(arr[i])

        if arr[i] == string[0:char]:
            res = canConstruct(string[char:len(string)], arr)
            if res == 1:
                return 1
    return 0
                
call1 = canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], )
call2 = canConstruct("skateboard",["ate", "rd", "boar", "bo", "sk", "ska"], )
call3 = canConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"], )

print(call1, call2)
print(call3) 
