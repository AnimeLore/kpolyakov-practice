reg = input("Введите выражение:\n")
print("Ответ:", eval(reg))
reg = list(reg)
o = ""
for k in range(0, len(reg)):
    if reg[k] == "+" or reg[k] == "-":
        break
    o += reg[k]
o = int(o)
for i in range(len(reg)):
    if reg[i] == "+" or reg[i] == "-":
        narg = ""
        for k in range(i + 1, len(reg)):
            if reg[k] == "+" or reg[k] == "-":
                break
            narg += reg[k]
        if reg[i] == "+":
            o += int(narg)
        if reg[i] == "-":
            o -= int(narg)
print("Ответ(цииклом):", o)
