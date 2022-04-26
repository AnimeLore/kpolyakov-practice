t = input()
sl = set(list(t))
for i in sl:
    print(f"\"{i}\": {t.count(i)}")
