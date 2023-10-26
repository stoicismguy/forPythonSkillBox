i = [int(x) for x in input().split(" ")]

def check(i):
    if i.count(i[0]) == len(i):
        return "Все числа равны"

    isRand = True
    for x in i:
        if i.count(x) > 1:
            isRand = False
    if isRand:
        return "Все числа разные"

    return "Есть равные и неравные числа"

print(check(i))
