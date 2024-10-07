import sys
input = sys.stdin.readline

n, m = map(int, input().split())
No_hear = []
No_see = []

for i in range(n):
    name1 = str(input().strip())
    No_hear.append(name1)
for j in range(m):
    name2 = str(input().strip())
    No_see.append(name2)

A = set(No_hear)
B = set(No_see)
C = A.intersection(B)
C = list(C)
C.sort()

print(len(C))
if len(C) != 0:
    for c in C:
        print(c)