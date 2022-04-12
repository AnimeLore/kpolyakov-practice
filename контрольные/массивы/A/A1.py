a = input().split()
print(len([i for i in a if i[-1] == '8' and int(i) % 3 == 0]))
