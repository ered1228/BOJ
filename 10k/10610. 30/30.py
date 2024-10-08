num = str(input())
N = [int(num[j]) for j in range(len(num))]
if sum(N) % 3 != 0:
    print(-1)
else:
    if 0 not in N:
        print(-1)
    else:
        N.sort(reverse=True)
        print(''.join(map(str, N)))