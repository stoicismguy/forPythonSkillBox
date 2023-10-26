a, b = map(int, input().split(" "))

def nod(a, b):
    if not (a != 0 and b != 0):
        return a + b

    if a > b:
        return nod(a % b, b)
    return nod(a, b % a)

print(nod(a, b))
