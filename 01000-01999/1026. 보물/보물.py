n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(n):
    Binx = B.index(max(B))
    Ainx = A.index(min(A))
    temp = A[Binx]
    A[Binx] = A[Ainx]
    A[Ainx] = temp
    res += A[Binx] * B[Binx]
    A.remove(A[Binx])
    B.remove(B[Binx])

print(res)