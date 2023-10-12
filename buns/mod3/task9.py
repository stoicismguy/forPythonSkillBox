def count(x, y, steps, way, part, oglen, length):
    if steps == 0:
        return x, y

    if way == 1:
        x -= 1
    if way == 2:
        y -= 1
    if way == 3:
        x += 1
    if way == 4:
        y += 1

    length -= 1
    steps -= 1

    if length == 0:
        if part == 1:
            part = 2
        else:
            part = 1
            oglen += 1

        way = (way + 1) % 5
        if way == 0: way = 1
        length = oglen
    return count(x, y, steps, way, part, oglen, length)


with open("input.txt") as f:
    n = int(f.readline())
    result = count(0, 0, n, 1, 1, 1, 1)
    with open("output.txt", "w") as out:
        out.write(f"{result[0]} {result[1]}")

