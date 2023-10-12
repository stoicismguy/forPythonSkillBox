desk = []
size = 0
while True:
    i = input()
    if i == "":
        break
    t = []
    for h in i:
        t.append(h)
    desk.append(t)
    size += 1


def checker(m):
    for row in range(len(m)):
        for char in "XO":
            if all([m[row][i] == char for i in range(len(m))]):
                return char

    for row in range(len(m)):
        for char in "XO":
            if all([m[i][row] == char for i in range(len(m))]):
                return char

    diagonal = []
    for i in range(len(m)):
        diagonal.append(m[i][i])

    for char in "XO":
        if all([i == char for i in diagonal]):
            return char

    diagonal = []
    for i in range(len(m)):
        diagonal.append(m[i][len(m)-i-1])

    for char in "XO":
        if all([i == char for i in diagonal]):
            return char

    return "Ничья"


print(checker(desk))
