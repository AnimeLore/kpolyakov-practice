a = list(input())
b = []
c = ""
i = 0
l = ["",0]
while i < len(a):
    if a[i] == " ":
        if c == "":
            i += 1
            continue
        else:
            if len(c) > l[1]:
                l[0] = c
                l[1] = len(c)
            b.append(c)
            c = ""
    else:
        c += a[i]
    i += 1
print(l[0],l[1])
