low, column = map(int, input().split())
S = []
for _ in range(low):
    S.append(str(input()))
for i in range(low-1, -1, -1):
    S.append(S[i])
for j in range(2*low):
    temp = S[j]
    S[j] = temp + temp[::-1]

a, b = map(int, input().split())
a -= 1
b -= 1
err_low = list(S[a])
if err_low[b] == '.':
    err_low[b] = '#'
else:
    err_low[b] = '.'
S[a] = ''.join(err_low)
for k in range(2*low):
    print(S[k])