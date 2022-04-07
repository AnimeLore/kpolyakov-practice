from random import randint

arr = [str(randint(-10, 10)) for i in range(6)]
k = 0
arr_o = []
print("Массив:\n" + " ".join(arr))
for i in arr:
    if int(i) <=0:
        arr_o.append(i)
    else:
        arr_o.insert(k,i)
        k+=1
print("Результат:\n" + " ".join(arr_o))