current = 11


def armstrong_generator():
    global current
    while True:
        if check(current):
            result = current
            current += 1
            yield result
        else:
            current += 1


def check(i: int):
    pow = len(str(i))
    return i == sum([int(x)**pow for x in str(i)])


def get_armstrong_numbers():
    return next(armstrong_generator())


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
