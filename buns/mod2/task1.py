i = input()
a = int(i[:i.find(",")])
b = int(i[i.find(",")+1::])
print(a%b)
