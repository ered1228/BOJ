from bisect import bisect_left

n = int(input())
S = [-float('inf')] + list(map(int, input().split()))
mv = [-float('inf')]

for i in range(1, n+1):
    temp = S[i]
    idx = bisect_left(mv, temp)
    if idx == len(mv):
        mv.append(temp)
    else:
        mv[idx] = temp
print(len(mv)-1)