romans = 'IVXLCDM'
values = [1, 5, 10, 50, 100, 500, 1000]


def rmn2arb(s):
    n, prev = 0, 100
    for c in s:
        pos = romans.index(c)
        if pos > prev:
            n -= 2 * values[prev]
        n += values[pos]
        prev = pos
    return str(n)


def chnR(s):
    w = s.split()
    o = False
    for i in range(len(w)):
        for j in w[i]:
            if romans.find(j) == -1:
                o = True
                break
        if o:
            o = False
            continue
        else:
            w[i] = rmn2arb(w[i])
    return " ".join(w)


t = input("Введите строку:\n")
print(f"Результат\n{chnR(t)}")
