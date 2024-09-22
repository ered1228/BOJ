n = int(input())
A = []
B = []
if n == 1:
    result = 0
else:
    for i in range(n):
        x, y = map(int, input().split())
        A.append(x)
        B.append(y)
    result = (max(A)-min(A))*(max(B)-min(B))
print(result)