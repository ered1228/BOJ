def tower(a, b, n): #a에서 b로 높이 n의 하노이 탑을 이동
    if n == 1:
        print(a, b)
        return
    tower(a, 6-a-b, n-1)
    print(a, b)
    tower(6-a-b, b, n-1)

n = int(input())
print((2**n)-1)
tower(1, 3, n)