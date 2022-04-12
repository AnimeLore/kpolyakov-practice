a = list(input())
b = []
c = ""
i = 0
while i < len(a):
    if a[i] == " ":
        if c == "":
            i += 1
            continue
        else:
            b.append(c)
            c = ""
    else:
        c += a[i]
    i += 1
print(len(b))
