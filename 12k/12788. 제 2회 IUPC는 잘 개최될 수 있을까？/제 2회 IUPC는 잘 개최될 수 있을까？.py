N = int(input())
t, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
p = 0 ; possible = False
for i in range(N):
    p += A[i]
    if p >= t*k:
        print(i+1)
        possible = True
        break
if not possible:
    print("STRESS")