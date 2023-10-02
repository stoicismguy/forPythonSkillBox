i = input().split(" ")
a = int(i[0])
b = int(i[1])
c = int(i[2])

if (min(a, b) == min(b, c)):
    print(min(a, c))
elif (min(a, c) == min(b, a)):
    print(min(b, c))
else:
    print(min(a, b))
