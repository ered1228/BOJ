from bisect import bisect_left

T = int(input())
for j in range(T):
    n, k = map(int, input().split())
    S = [0] + list(map(int, input().split()))
    mv = [0]

    for i in range(1, n+1):
        temp = S[i]
        idx = bisect_left(mv, temp)
        if idx == len(mv):
            mv.append(temp)
        else:
            mv[idx] = temp

    print(f"Case #{j+1}")
    if len(mv)-1 >= k:
        print(1)
    else:
        print(0)