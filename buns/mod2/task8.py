s = input()
i = input()
summ = 0
for j in range(len(s)):
    if s[j] == i:
        summ += 1
    else:
        break
print(summ)
