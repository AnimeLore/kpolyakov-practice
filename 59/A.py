print("Введите 5 строк:")
arr = [input(f"{i+1}. ") for i in range(5)]
print(", ".join(sorted(arr)))
