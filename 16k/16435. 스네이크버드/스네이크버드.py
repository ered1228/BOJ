n, l = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

if l < H[0]:
    print(l)
else:
    for i in range(n):
        if H[i] <= l:
            l += 1
        else:
            break
    print(l)