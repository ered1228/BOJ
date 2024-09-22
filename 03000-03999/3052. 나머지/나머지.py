A = []
for _ in range(10):
    n = int(input())
    a = n % 42
    A.append(a)
B = set(A)
print(len(B))