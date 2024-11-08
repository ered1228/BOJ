from collections import deque

def ISD(jururu, gosegu):
    v = set()
    q = deque([(0, 0, 1)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ISDmatrix = [[0]*gosegu for _ in range(jururu)]
    while q:
        x, y, cnt = q.popleft()
        if (x, y) not in v:
            v.add((x, y))
            for i in range(4):
                nx = x + dx[i] ; ny = y + dy[i]
                if 0 <= nx < gosegu and 0 <= ny < jururu and lilpa[ny][nx] == 1:
                    if ISDmatrix[ny][nx] == 0 or cnt+1 < ISDmatrix[ny][nx]:
                        ISDmatrix[ny][nx] = cnt+1
                        q.append((nx, ny, cnt+1))
    return ISDmatrix[jururu-1][gosegu-1]

jururu, gosegu = map(int, input().split())
lilpa = []

for _ in range(jururu):
    ine = str(input())
    jingburger = []
    for r in ine:
        jingburger.append(int(r))
    lilpa.append(jingburger)
    
viichan = ISD(jururu, gosegu)
print(viichan)