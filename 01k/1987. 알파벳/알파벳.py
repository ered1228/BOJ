def travel(i, j, depth):
    global cnt
    cnt = max(cnt, depth)
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < r and 0 <= nj < c:
            char = ord(board[ni][nj])-65
            if A[char]:
                A[char] = False
                travel(ni, nj, depth+1)
                A[char] = True

r, c = map(int, input().split())
board = []
for _ in range(r):
    S = str(input())
    board.append([S[k] for k in range(c)])

cnt = 0
A = [True]*26
A[ord(board[0][0])-65] = False
travel(0, 0, 1)
print(cnt)