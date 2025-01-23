def cut(mid, tree):
    res = 0
    for t in tree:
        if t > mid:
            res += t-mid
    return res

n, m = map(int, input().split())
tree = list(map(int, input().split()))
mid = sum(tree) // n
start = 0
end = 2*(10**9)

while True:
    if cut(mid, tree) == m or mid == 0 or end < start:
        print(mid)
        break
    elif cut(mid, tree) > m:
        start = mid + 1
        mid = (start + end) // 2
    else:
        end = mid - 1
        mid = (start + end) // 2