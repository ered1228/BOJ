A = [0, 1]
n = int(input())
if n <= 1:
    print(A[n])
else:
    for i in range(2, n+1):
        A.append(A[i-1] + A[i-2])
    print(A[n])