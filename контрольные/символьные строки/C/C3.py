arr = list(input())
dl = False
for k in range(len(arr)):
    if not dl:
        if arr[k] == "<":
            arr[k] = ""
            dl = not dl
        continue
    else:
        if arr[k] == ">":
            dl = not dl

        arr[k] = ""
print("".join(arr))
