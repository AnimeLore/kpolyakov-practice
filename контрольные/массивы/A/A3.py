from random import randint
arr = [str(randint(0, 50)) for i in range(20)]
print(" ".join(arr))
t = arr.pop()
out = False
print("Номера всех элементов, равных последнему элементу:")
for k in range(len(arr)):
    if arr[k] == t:
        print(f"A[{k+1}]={t}")
        out = True
if not out:
    print("Таких элементов нет")
