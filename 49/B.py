from random import randint
import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


arr = [str(randint(0, 100)) for i in range(6)]
print("Массив A:\n" + " ".join(arr))
arr_o = [i for i in arr if is_prime(int(i))]
print("Массив B:\n" + " ".join(arr_o))
