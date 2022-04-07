from random import randint

arr = [str(randint(-10, 10)) for i in range(6)]
print("Массив A:\n" + " ".join(arr))
arr_o = [i for i in arr if int(i) % 2 == 0 and int(i) < 0]
print("Массив B:\n" + " ".join(arr_o))
