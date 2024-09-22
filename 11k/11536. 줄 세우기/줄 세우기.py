def same(A, B, n):
    for i in range(n):
        if A[i] != B[i]:
            return False
    return True

n = int(input())
A = []
B = []

for _ in range(n):
    A.append(str(input()))

B = A.copy()
B.sort()
if same(A, B, n):
    print("INCREASING")
else:
    B.sort(reverse = True)
    if same(A, B, n):
        print("DECREASING")
    else:
        print("NEITHER")