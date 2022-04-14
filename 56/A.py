reg = input("Введите выражение:\n")
print("Ответ:",eval(reg))
reg = reg.split("+")
o=0
for i in reg:
    o+=int(i)
print("Ответ(цииклом):",o)