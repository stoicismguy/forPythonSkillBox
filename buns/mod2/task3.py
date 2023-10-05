i = input()
symbpol1 = i.find(" ")
i = i.replace(" ", "", 1)
symbpol2 = i.find(" ")
a = int(i[:symbpol1:])
b = int(i[symbpol1:symbpol2:])
c = int(i[symbpol2+1::])

if (min(a, b) == min(b, c)):
    print(min(a, c))
elif (min(a, c) == min(b, a)):
    print(min(b, c))
else:
    print(min(a, b))
