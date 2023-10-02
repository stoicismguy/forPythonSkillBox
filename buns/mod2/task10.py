i = input()
result = ""
for j in range(len(i)-1):
    if i[j+1] == " ":
        result += i[j]
    if j == len(i)-2:
        result += i[j+1]
print(result)

        
