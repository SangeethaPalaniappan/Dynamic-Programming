# Fibonacci Sequence - Tabulation

n = int(input("n : "))
arr = [0] * (n + 1)
arr[1] = 1
i = 2

for k in range(n - 1):
    arr[i] = arr[i - 1] + arr[i - 2]
    i += 1
print(arr[n])

# Time Complexity  :  O(N)
# Space Complexity : O(N)