def prime(n):
    A = [False, False] + [True]*(2*n-1)
    for i in range(2, 2*n+1):
        if A[i]:
            for j in range(i*2, 2*n+1, i):
                A[j] = False
    A = A[n+1:]
    return A.count(True)

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(prime(n))