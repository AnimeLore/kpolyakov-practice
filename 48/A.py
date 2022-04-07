from random import randint

arr = [str(randint(0, 9)) for i in range(6)]
print("Массив:\n" + " ".join(arr))
t = [arr[-1]]
del arr[-1]
t += arr
print("Результат:\n" + " ".join(t))
