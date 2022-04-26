import random

j = 0
arr = [[None for i in range(4)] for i in range(3)]
coords = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1), (1, 2)]
for k in coords:
    j += 1
    x, y = k
    arr[x][y] = str(j)
for k in arr:
    print(" ".join(k))
