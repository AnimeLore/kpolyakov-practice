a = list(map(int,input().split()))
b = []
for k in a:
    c = f'{k:b}'
    if len(c) %2 == 0:
        if c[0:(len(c)//2)] == (c[(len(c)//2+1):len(c)])[::-1]:
            b.append(k)
    else:
        if c[0:(len(c)//2)] == (c[(len(c)//2+1):len(c)])[::-1]:
            b.append(k)
print(len(b))