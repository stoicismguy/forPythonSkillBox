b, p = map(int, input().split(" "))

def pow(base, exp):
    if exp <= 1:
        return base

    if exp % 2 == 0:
        return pow(base**2, exp/2)
    else:
        return base * pow(base, exp - 1)


print(pow(b, p))
