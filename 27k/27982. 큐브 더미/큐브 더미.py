n, m = map(int, input().split())
C = []
cnt = 0

if m < 0:
    print(0)
else:
    for _ in range(m):
        c = list(map(int, input().split()))
        C.append(c)
    for c in C:
        t1 = [c[0]+1, c[1], c[2]]
        t2 = [c[0]-1, c[1], c[2]]
        t3 = [c[0], c[1]+1, c[2]]
        t4 = [c[0], c[1]-1, c[2]]
        t5 = [c[0], c[1], c[2]-1]
        t6 = [c[0], c[1], c[2]+1]
        if t1 in C:
            if t2 in C:
                if t3 in C:
                    if t4 in C:
                        if t5 in C:
                            if t6 in C:
                                cnt += 1
    print(cnt)