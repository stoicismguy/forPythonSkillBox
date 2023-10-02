n = input()
m = int(input())
code = ord(n) + m
a = ord("a")
if m >= 0:
    print(chr(((ord(n) - a + m) % 26) + a))
else:
    print(chr(((ord(n) - a - m) % 26) + a))
