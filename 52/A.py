from random import randint


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
arr = qs(arr[:4], 0, 3) + qs(arr[4:8], 0, 3)
print("После сортировки:")
print(arr)
