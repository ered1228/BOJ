n = int(input())
a1 = int(input())
A = [a1]
for i in range(n-1):
    a = int(input())
    A.append(max(a, A[i]+a))
print(max(A))