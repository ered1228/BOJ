def find_square(i, j):
    return ((i - 1) // 3) * 3 + (j - 1) // 3 + 1

def backtracking(zero, start):
    if start == len(zero):
        for r in res:
            print(' '.join(map(str, r)))
        exit()
        return
    
    r, c = zero[start]
    for v in range(1, 10):
        if not col[c][v] and not row[r][v]:
            s = find_square(r, c)
            if not square[s][v]:
                res[r-1][c-1] = v
                col[c][v] = True
                row[r][v] = True
                square[s][v] = True
                
                backtracking(zero, start+1)
                res[r-1][c-1] = 0
                col[c][v] = False
                row[r][v] = False
                square[s][v] = False

zero = []
col = [[False]*10 for _ in range(10)]
row = [[False]*10 for _ in range(10)]
square = [[False]*10 for _ in range(10)]
res = []

for i in range(1, 10):
    R = list(map(int, input().split()))
    for j, val in enumerate(R, start=1):
        if val == 0:
            zero.append((i, j))
        else:
            row[i][val] = True
            col[j][val] = True
            s = find_square(i, j)
            square[s][val] = True
    res.append(R)

backtracking(zero, 0)