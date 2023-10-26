i = input()
with open(i) as f:
    line = f.readline()
    dic = {}
    for s in line:
        if s not in dic.keys():
            dic[s] = 1
        else:
            dic[s] += 1
    sorted_dic = reversed(sorted(dic.items(), key=lambda item: item[1]))
            
    with open("", 'w') as w:
        for s, v in sorted_dic:
            w.write(f"{s} {w}")
