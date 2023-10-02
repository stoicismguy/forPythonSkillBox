i = input()
current = ""
for j in range(len(i)-1, -2, -1):
    if i[j] == "." or j == -1:
        print(current[::-1])
        current = ""
    else:
        current += i[j]


