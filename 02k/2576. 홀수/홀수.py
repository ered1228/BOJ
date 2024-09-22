A = []

for i in range(7):
    n = int(input())
    if n % 2 == 1: #홀수
        A.append(n)

if len(A) == 0:
    print("-1")
else:
    print(sum(A))
    print(min(A))