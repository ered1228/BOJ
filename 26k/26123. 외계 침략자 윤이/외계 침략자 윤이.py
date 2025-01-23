from collections import defaultdict, deque

n, d = map(int, input().split())
A = list(map(int, input().split()))
building = defaultdict(int)
for a in A:
    building[a] += 1

cnt = 0
B = [list(b) for b in building.items()]
B.sort(reverse = True)
B = deque(B)
l = len(A)
for i in range(d):
    num, c = B.popleft()
    if num == 0 and c == l:
        break
    cnt += c
    num -= 1
    if len(B) > 0 and num == B[0][0]:
        B[0][1] += c
    else:
        B.appendleft([num, c])
print(cnt)