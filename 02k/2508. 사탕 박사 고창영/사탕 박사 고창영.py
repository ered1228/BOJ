import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    l = input()
    r, c = map(int, input().split())
    box = [] ; O = [] ; cnt = 0
    
    for i in range(r):
        candy = [s for s in str(input().strip())]
        for j in range(c):
            if candy[j] == 'o':
                O.append((i, j))
        box.append(candy)
    
    for x, y in O:
        if 0 <= x < r and 1 <= y < c-1:
            if box[x][y-1] == '>' and box[x][y+1] == '<':
                cnt += 1
        if 1 <= x < r-1 and 0 <= y < c:
            if box[x-1][y] == 'v' and box[x+1][y] == '^':
                cnt += 1
    print(cnt)