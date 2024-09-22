n = int(input())
lotto = str(input())

A = [ord(lotto[0])]
cnt = 1
res = 'NO'

for i in range(1, n):
    num = ord(lotto[i])
    A.append(num)
    if abs(A[i-1] - A[i]) == 1:
        cnt += 1
        if cnt == 5:
            res = 'YES'
            break
    else:
        cnt = 1

print(res)