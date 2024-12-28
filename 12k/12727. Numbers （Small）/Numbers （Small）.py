import math

def cal(n):
    if n == 1:
        return '005'
    elif n == 2:
        return '027'
    elif n > 15:
        data = ['991', '095', '607', '263', '151', '855', '527', '743', '351', '135',
                '407', '903', '791', '135', '647']
        return data[n-16]
    else:
        dp = [0, 5.2360679775, 27.416407865]
        for i in range(3, n+1):
            dp.append((6*dp[i-1]) - (4*dp[i-2]))
        res = str(int(dp[n])%1000)
        if len(res) == 1:
            res = '00' + res
        elif len(res) == 2:
            res = '0' + res
        return res

t = int(input())
for i in range(1, t+1):
    n = int(input())
    res = cal(n)
    print(f"Case #{i}: {res}")