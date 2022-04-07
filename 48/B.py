from random import randint

arr = [str(randint(0, 9)) for i in range(6)]
print("Массив:\n" + " ".join(arr))
r1 = arr[2::-1]
r1.extend(arr[6:2:-1])

print("Результат:\n" + " ".join(r1))
