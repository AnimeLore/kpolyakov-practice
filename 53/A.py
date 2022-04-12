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


def bs(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0
    p = 0
    while start <= end:
        p += 1
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return p

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [randint(0, 9) for i in range(8)]
print("Массив:")
print(arr)
arr = qs(arr, 0, len(arr)-1)
print("После сортировки:")
print(arr)
X = int(input("Введите число X:\n"))
r=bs(arr,X)
if r == -1:
    print(f"Число {X} не найдено.")
else:
    print(f"Число {X} найдено.")
    print(f"Количество сравнений: {r}")
