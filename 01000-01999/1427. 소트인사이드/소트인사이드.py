n = str(input())
A = [n[i] for i in range(len(n))]

A.sort(reverse = True)
for j in range(len(A)):
    print(A[j], end='')