from random import randint

arr = [str(randint(0, 9)) for i in range(6)]
print("Массив:\n" + " ".join(arr))
print("Результат:\n"+" ".join(sorted(arr, reverse=True)))