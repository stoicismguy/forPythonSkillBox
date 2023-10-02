i = input().replace(" ", "")

def checker(i):
    for j in i:
        if i.count(j) != 1:
            return False
    return True

print(checker(i))


