n = int(input())
A = [0]*(50001)
S = [0]

for i in range(1, 224):
    sq = i*i
    A[sq] = 1
    S.append(sq)
    A[sq+1] = 2
    if sq*2 < 50001:
        A[sq*2] = 2

S.append(224*224)
for j in range(1, n+1):
    if A[j] == 0:
        val = 4
        k = 1
        while S[k] < j:
            val = min(val, A[S[k]]+A[j-S[k]])
            k += 1
        else:
            A[j] = val

print(A[n])