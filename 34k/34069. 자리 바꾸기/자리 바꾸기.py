n, m = map(int, input().split())
ori_num = []
for _ in range(n):
    ori_num.append(list(map(int, input().split())))

if n*m % 2 != 0:
    print("No")
else:
    print("Yes")
    if n%2 == 0:
        for i in range(0, n, 2):
            temp = ori_num[i]
            ori_num[i] = ori_num[i+1]
            ori_num[i+1] = temp
    else:
        for i in range(n):
            for j in range(0, m, 2):
                temp = ori_num[i][j]
                ori_num[i][j] = ori_num[i][j+1]
                ori_num[i][j+1] = temp
    
    for row in ori_num:
        print(' '.join(map(str, row)))