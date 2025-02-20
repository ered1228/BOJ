n = int(input())
cnt = 0
for i in range(1, n+1): 
    if i // 10 == 0:
        cnt += 1
        continue
    
    i = list(map(int, str(i)))
    s = True
    d = i[1] - i[0]
    for j in range(1, len(i)):
        nd = i[j] - i[j-1]
        if d != nd:
            s = False
            break
    if s:
        cnt += 1
print(cnt)