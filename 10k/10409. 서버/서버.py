n, t = map(int, input().split())
A = list(map(int, input().split()))
A_sum = 0
cnt = 0
for i in range(n):
    A_sum += A[i]
    if A_sum <= t:
        cnt += 1
    else:
        break
print(cnt)