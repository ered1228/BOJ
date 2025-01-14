def n_queens(board, row):
    global cnt
    if row == n:
        cnt += 1
    for col in range(n):
        if no_check(board, row, col, col_check, dia1_check, dia2_check):
            board[row][col] = 1
            col_check[col] = True
            dia1_check[row+col] = True
            dia2_check[row-col+n-1] = True
            n_queens(board, row+1)
            
            #backtracking
            board[row][col] = 0
            col_check[col] = False
            dia1_check[row+col] = False
            dia2_check[row-col+n-1] = False

def no_check(board, row, col, col_check, dia1_check, dia2_check):
    if col_check[col] or dia1_check[row+col] or dia2_check[row-col+n-1]:
        return False
    return True

n = int(input())
col_check = [False]*(n)
dia1_check = [False]*(2**n)
dia2_check = [False]*(2**n)
cnt = 0
board = [[0]*n for _ in range(n)]
n_queens(board, 0)
print(cnt)