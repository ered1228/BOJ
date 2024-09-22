import sys
input = sys.stdin.readline
S = []
I = []
temp = 0

for _ in range(8):
    score = int(input())
    S.append(score)

for _ in range(5):
    temp += max(S)
    inx = S.index(max(S))
    I.append(inx+1)
    S[inx] = -1

I.sort()    
print(temp)
print(*I)