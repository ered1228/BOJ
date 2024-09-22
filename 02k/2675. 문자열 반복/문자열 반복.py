t = int(input())

for i in range(t):
    n, A = input().split()
    n = int(n)
    A = str(A)
    for j in range(len(A)):
        print(A[j]*n, end="")
    print("")    