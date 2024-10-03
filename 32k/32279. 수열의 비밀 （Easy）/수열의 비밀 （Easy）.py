n = int(input())
p, q, r, s = map(int, input().split())
a1 = int(input())
A = [0, a1]
if n == 1:
    print(a1)
else:
    for i in range(1, 11):
        A.append(A[i]*p + q)
        A.append(A[i]*r + s)
    A = A[:n+1]
    print(sum(A))