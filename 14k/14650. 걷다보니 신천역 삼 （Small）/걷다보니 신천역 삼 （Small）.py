n = int(input())
A = ['0', '1', '2']
if n == 1:
    print(0)
elif n == 2:
    print(2)
elif n == 3:
    print(6)
elif n == 4:
    cnt = 0
    for i in range(1, 3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    temp = A[i]+A[j]+A[k]+A[l]
                    if int(temp) % 3 == 0:
                        cnt += 1
    print(cnt)
elif n == 5:
    cnt = 0
    for i in range(1, 3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        temp = A[i]+A[j]+A[k]+A[l]+A[m]
                        if int(temp) % 3 == 0:
                            cnt += 1
    print(cnt)
elif n == 6:
    cnt = 0
    for i in range(1, 3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for o in range(3):
                            temp = A[i]+A[j]+A[k]+A[l]+A[m]+A[o]
                            if int(temp) % 3 == 0:
                                cnt += 1
    print(cnt)
elif n == 7:
    cnt = 0
    for i in range(1, 3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for o in range(3):
                            for p in range(3):
                                temp = A[i]+A[j]+A[k]+A[l]+A[m]+A[o]+A[p]
                                if int(temp) % 3 == 0:
                                    cnt += 1
    print(cnt)
elif n == 8:
    cnt = 0
    for i in range(1, 3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for o in range(3):
                            for p in range(3):
                                for q in range(3):
                                    temp = A[i]+A[j]+A[k]+A[l]+A[m]+A[o]+A[p]+A[q]
                                    if int(temp) % 3 == 0:
                                        cnt += 1
    print(cnt)
else:
    cnt = 0
    for i in range(1, 3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for o in range(3):
                            for p in range(3):
                                for q in range(3):
                                    for r in range(3):
                                        temp = A[i]+A[j]+A[k]+A[l]+A[m]+A[o]+A[p]+A[q]+A[r]
                                        if int(temp) % 3 == 0:
                                            cnt += 1
    print(cnt)