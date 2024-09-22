import sys
input = sys.stdin.readline

C = [[0]*1000, []]

n = int(input())
for _ in range(n):
    title = str(input())
    if title in C[1]:
        inx = C[1].index(title)
        C[0][inx] += 1
    else:
        C[1].append(title)
        inx = C[1].index(title)
        C[0][inx] += 1
        
m = max(C[0])
N = [C[1][i] for i in range(len(C[1])) if C[0][i] == m]
N.sort()
print(N[0])