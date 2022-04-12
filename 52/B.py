from random import randint
from collections import Counter


def qs(a, s, e):
    if s >= e: return a
    L = s
    R = e
    X = a[(L + R) // 2]
    while L <= R:
        while a[L] < X:
            L += 1
        while a[R] > X:
            R -= 1
        if L <= R:
            a[L], a[R] = a[R], a[L]
            L += 1
            R -= 1
        a = qs(a, s, R)
        a = qs(a, L, e)
    return a


arr = [randint(0, 9) for i in range(8)]
print("Массив:")
print(arr)
arr = qs(arr, 0, 7)
print("После сортировки:")
print(arr)
unique = 0
brr = Counter(arr)
for k in brr:
    if brr[k] == 1:
        unique+=1
print(f"Различных чисел: {unique}")
