i = input()
even_s = 0
odd_s = 0
for j in range(len(i)):
    if j % 2 == 0:
        even_s += int(i[j])
    else:
        odd_s += int(i[j])
        
if (even_s + 3 * odd_s) % 10 == 0:
    print("yes")
else:
    print("no")
