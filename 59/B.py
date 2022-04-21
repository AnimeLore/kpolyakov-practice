print("Введите ФИО:")
arr = []
while True:
    cs = input()
    if cs == "":
        break
    arr.append(cs)
arr.sort(key=lambda elem:elem[5:])
print("\nСписок в алфавитном порядке:")
print("\n".join(arr))