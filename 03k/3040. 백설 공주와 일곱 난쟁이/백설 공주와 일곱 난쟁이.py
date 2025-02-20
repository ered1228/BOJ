dwarfs = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i+1, 9):
        t1, t2 = dwarfs[i], dwarfs[j]
        dwarfs[i], dwarfs[j] = 0, 0
        if sum(dwarfs) == 100:
            for d in dwarfs:
                if d != 0:
                    print(d)
            exit()
        dwarfs[i], dwarfs[j] = t1, t2