def sol(temp, l):
    if l == m:
        print(' '.join(map(str, temp)))
        return
    else:
        for i in range(n):
            if J[i]:
                temp.append(A[i])
                J[i] = False
                sol(temp, l+1)
                temp.pop()
                J[i] = True

n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
J = [True]*n
temp = []
sol(temp, 0)