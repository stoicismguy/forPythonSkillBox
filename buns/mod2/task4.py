n = float(input())
if int(n) == n:
    n = int(n)
    print(f"{bin(n)[2:]}, {oct(n)[2:]}, {hex(n)[2:]}")
else:
    print("Неверный ввод")
