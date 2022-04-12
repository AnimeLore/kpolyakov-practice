a = list(input())
for k in range(len(a)):
    if a[k] == "а":
        a[k] = "б"
    elif a[k] == "А":
        a[k] = "Б"
    elif a[k] == "Б":
        a[k] = "А"
    elif a[k] == "б":
        a[k] = "а"
print("".join(a))
