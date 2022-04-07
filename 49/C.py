from random import randint

fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
arr = [str(randint(0, 100)) for i in range(6)]
print("Массив A:\n" + " ".join(arr))
arr_o = [i for i in arr if int(i) in fib]
print("Массив B:\n" + " ".join(arr_o))
