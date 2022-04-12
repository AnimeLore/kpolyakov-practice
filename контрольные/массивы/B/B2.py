from random import randint

def q(a):
    return sum(list(map(int,list(a))))
def qs(a, s, e):
    if s >= e: return a
    L = s
    R = e
    X = a[(L + R) // 2]
    while L <= R:
        while q(a[L]) < q(X):
            L += 1
        while q([R]) > q(X):
            R -= 1
        if L <= R:
            a[L], a[R] = a[R], a[L]
            L += 1
            R -= 1
        a = qs(a, s, R)
        a = qs(a, L, e)
    return a


arr = [str(randint(100, 999)) for i in range(8)]
print(" ".join(arr))
print(" ".join(qs(arr, 0, 7)))
