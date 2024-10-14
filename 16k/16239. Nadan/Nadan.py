k = int(input())
n = int(input())
if n == 1:
    print(k)
else:
    A = [1]
    for j in range(n-2):
        A.append(j+2)
    A.append(k-sum(A))
    for a in A:
        print(a)