arr = [list(map(int,input().split())) for i in range(4)]
xmx, ymx, xmn, ymn = 0, 0,0,0
mx = 0
mn = 100
for i in range(len(arr)):
    if max(arr[i]) > mx:
        mx = max(arr[i])
        xmx = i + 1
        ymx = arr[i].index(mx) + 1
    if min(arr[i]) < mn:
        mn = min(arr[i])
        xmn = i + 1
        ymn = arr[i].index(mn) + 1
print(f"Максимальный элемент A[{xmx},{ymx}]={mx}")
print(f"Минимальный элемент A[{xmn},{ymn}]={mn}")
