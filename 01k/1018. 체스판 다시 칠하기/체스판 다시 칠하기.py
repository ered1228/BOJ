def count_chess(B):
    cnt1, cnt2 = 0, 0
    for i in range(8):
        for j in range(8):
            if B[i][j] != B1[i][j]:
                cnt1 += 1
            if B[i][j] != B2[i][j]:
                cnt2 += 1
    return min(cnt1, cnt2)
          
n, m = map(int, input().split())
B1 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 
      'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
B2 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 
      'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
chess = []
res = []

for _ in range(n):
    board = str(input())
    chess.append(board)
    
for i in range(0, n-7):
    for j in range(0, m-7):
        B = [r[j:j+8] for r in chess[i:i+8]]
        res.append(count_chess(B))

print(min(res))