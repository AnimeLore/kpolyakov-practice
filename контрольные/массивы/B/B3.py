from random import randint

arr = [randint(0, 1000) for i in range(20)]
print(" ".join(list(map(str, arr))))
m = 0
j = 0
for k in range(len(arr) - 1):
    if arr[k] * arr[k + 1] > m:
        m = arr[k] * arr[k + 1]
        j = k + 1
print(j, j + 1)
