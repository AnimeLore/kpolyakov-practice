arr = [list(map(int, input().split())) for i in range(4)]
sr = 0
for k in arr:
    for i in k:
        sr += i
sr /= len(arr) * len(arr[0])
print(f"Средняя яркость {sr:.2f}")
print("Результат:")
for k in range(len(arr)):
    for i in range(len(arr[k])):
        if arr[k][i] < sr:
            arr[k][i] = "  0"
        else:
            arr[k][i] = "255"
    print(" ".join(arr[k]))
