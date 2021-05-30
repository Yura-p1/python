a = 2
b = 3
i = 0
while a <= b:
    a = a * 0.1 + a
    if a < 3:
        i += 1
    print("Шаг:",i,")", format(f"{a:.2f}"))
