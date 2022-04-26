arr = [list(map(int, input().split())) for i in range(4)]
ud_arr = [[None for j in range(len(arr[0]))] for k in range(len(arr))]

for i in range(len(arr[0])):
    for k in range(len(arr)-1,-1,-1):
        ud_arr[i].append(arr[k][i])
        print(f"{arr[k][i]:4d}", end="")
    print()

