A = []
while True:
    A = list(map(int, input().split()))
    if sum(A) ==0:
        break
    max_n = max(A)
    A.remove(max_n)
    if A[0]**2 + A[1]**2 == max_n**2:
        print("right")
    else:
        print("wrong")