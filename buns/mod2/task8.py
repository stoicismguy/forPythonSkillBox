n = input()
s = n[:n.find(","):]
i = n[n.find(",")+1::]
summ = 0
for j in range(len(s)):
    if s[j] == i:
        summ += 1
    else:
        break
print(summ)
