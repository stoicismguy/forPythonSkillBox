i = input()

def canBePalindrome(i: str):
    isend = False
    odd = 0
    a = []
    for item in i:
        if item not in a:
            if i.count(item) % 2 != 0:
                odd += 1
            a.append(item)
    if odd != 1 and odd != 0:
        isend = True

    if not isend:
        return True
    else:
        return False


def makePalindrome(i):
    a = []
    odd = ''
    for item in i:
        if item not in a:
            if i.count(item) % 2 != 0:
                odd = item
            else:
                a.append(item)
    result = odd * i.count(odd)

    for s in a:
        result = s * (i.count(s)//2) + result + s * (i.count(s)//2)
    return result


if canBePalindrome(i):
    print(makePalindrome(i))
else:
    print("Не может быть палиндромом")
