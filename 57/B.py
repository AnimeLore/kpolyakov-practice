fn = input("Введите название файла: ")
r = input("Введите Новое расширение: ")
print("Результат:", ".".join(fn.split(".")[:len(fn.split("."))-1]) + "." + r)