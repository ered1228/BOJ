dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

t1 = 0
t2 = 0
find = False
for i in range(9):
    for j in range(i+1, 9):
        t1 = dwarf[i]
        t2 = dwarf[j]
        dwarf[i] = 0
        dwarf[j] = 0
        if sum(dwarf) == 100:
            find = True
            break
        else:
            dwarf[i] = t1
            dwarf[j] = t2
    if find:
        break
        
dwarf.sort()
dwarf = dwarf[2:]
for d in dwarf:
    print(d)