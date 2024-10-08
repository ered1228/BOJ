n = int(input())
A = []
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    A.append((a, b))
A.sort(key=lambda x : x[1])
print(A[0][0])