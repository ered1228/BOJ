def sol(A, temp):
    if len(temp) == m:
        seq.add(tuple(temp))
        return
    else:
        for i in range(n):
            if not J[i]:
                J[i] = True
                temp.append(A[i])
                sol(A, temp)
                temp.pop()
                J[i] = False

n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
seq = set() ; J = [False]*n
sol(A, [])
seq = sorted(list(seq))
for s in seq:
    print(' '.join(map(str, s)))