from collections import deque
import sys
input = sys.stdin.readline

def ISD(lilpa):
    visited = [False]*ine
    queue = deque([(lilpa, 0)])
    visited[lilpa] = True
    cnt = 0
    while queue:
        num, dist = queue.popleft()
        if dist > 1:
            continue
        for i, f in enumerate(jingburger[num]):
            if f == 'Y' and not visited[i]:
                visited[i] = True
                queue.append((i, dist + 1))
                cnt += 1
    return cnt

ine = int(input())
jingburger = [] ; viichan = 0
for _ in range(ine):
    jingburger.append([jururu for jururu in str(input())])

for lilpa in range(ine):
    gosegu = ISD(lilpa)
    viichan = max(viichan, gosegu)
print(viichan)
