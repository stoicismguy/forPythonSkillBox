i = int(input())
print(bin(i)[2:], oct(i)[2:], hex(i)[2:]) if i >= 0 else print("Неверный ввод")
