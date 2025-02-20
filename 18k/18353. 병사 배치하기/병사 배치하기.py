from bisect import bisect_left

n = int(input())
S = list(map(int, input().split()))
S = [0] + list(reversed(S))
mv = [0]

for i in range(1, n+1):
    temp = S[i]
    idx = bisect_left(mv, temp)
    if idx == len(mv):
        mv.append(temp)
    else:
        mv[idx] = temp
print(n-len(mv)+1)