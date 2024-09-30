import sys
input = sys.stdin.readline

sumA = []
divA = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    sumA.append(a+b)
    divA.append(a-b)

sumA.sort()
divA.sort()
c = abs(sumA[-1] - sumA[0])
d = abs(divA[-1] - divA[0])
print(max(c, d))