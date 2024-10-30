import sys
input = sys.stdin.readline

n = int(input())
A = [float(input())]
for _ in range(n-1):
    a = float(input())
    if A[-1] > 1:
        A.append(a*A[-1])
    else:
        A.append(a)
print(f"{max(A):.3f}")