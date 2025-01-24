n = int(input())
statue = list(map(int, input().split()))
st = statue[0]
dp1 = [1] + [0]*(n-1)
dp2 = [0]*n
m = 0
for i in range(1, n):
    if statue[i] == statue[i-1] and statue[i] == st:
        dp1[i] = dp1[i-1]+1
        dp2[i] = max(0, dp2[i-1]-1)
    elif statue[i] == statue[i-1] and statue[i] != st:
        dp1[i] = max(0, dp1[i-1]-1)
        dp2[i] = dp2[i-1]+1    
    elif statue[i] != statue[i-1] and statue[i] == st:
        dp1[i] = dp1[i-1]+1
        dp2[i] = dp2[i-1]-1
    else:
        dp1[i] = dp1[i-1]-1
        dp2[i] = dp2[i-1]+1
for j in range(n):
    m = max(dp1[j], dp2[j], m)
print(m)