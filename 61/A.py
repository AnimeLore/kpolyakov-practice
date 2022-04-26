arr = [list(map(int, input().split())) for i in range(4)]
for k in range(len(arr)):
    for i in range(len(arr[k])):
        if i > k:
            arr[k][i] = 0
        print(f"{arr[k][i]:4d}", end="")
    print()
