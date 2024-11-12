from bisect import bisect_left

n, l = map(int, input().split())
hole = list(map(int, input().split()))

hole.sort()
cnt = 0
start = hole[0] - 0.5
end = start + l

while True:
    idx = bisect_left(hole, end)
    if idx == n:
        break
    else:
        start = hole[idx] - 0.5
        end = start + l
        cnt += 1

print(cnt+1)