def cross_product_2D(a, b):
    return a[0]*b[1] - a[1]*b[0]

def watch(A, i):
    cnt = 0
    if i == 0:
        x = 1
        initial_v = [1, A[1]-A[0], 0]
        while x <= n-2:
            next_v = [x+1, A[x+1]-A[0], 0]
            if cross_product_2D(initial_v, next_v) > 0:
                cnt += 1
                initial_v = next_v
            x += 1
        return cnt+1
    elif i == (n-1):
        x = n-2
        initial_v = [-1, A[n-2]-A[n-1], 0]
        while x >= 1:
            next_v = [x-n, A[x-1]-A[n-1], 0]
            if cross_product_2D(initial_v, next_v) < 0:
                cnt += 1
                initial_v = next_v
            x -= 1
        return cnt+1
    else:
        x = i+1
        initial_v = [1, A[i+1]-A[i], 0]
        while x <= n-2:
            next_v = [x-i+1, A[x+1]-A[i], 0]
            if cross_product_2D(initial_v, next_v) > 0:
                cnt += 1
                initial_v = next_v
            x += 1
        x = i-1
        initial_v = [-1, A[i-1]-A[i], 0]
        while x >= 1:
            next_v = [x-(i+1), A[x-1]-A[i], 0]
            if cross_product_2D(initial_v, next_v) < 0:
                cnt += 1
                initial_v = next_v
            x -= 1
        return cnt+2

n = int(input())
building = list(map(int, input().split()))
if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(n-1)
else:
    res = []
    for i in range(n):
        res.append(watch(building, i))
    print(max(res))