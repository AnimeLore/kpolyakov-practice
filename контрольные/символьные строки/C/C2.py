words = input().split()
w = {}
for i in words:
    if i[0] in w.keys():
        w[i[0]] += 1
    else:
        w[i[0]] = 1
for i in w.keys():
    t = ["", "а"][w[i] in (2, 3, 4)]
    t = [t, ["", "о"][w[i] == 1]][t == ""]
    print(f"На букву \"{i}\" начинается {w[i]} слов{t}")
