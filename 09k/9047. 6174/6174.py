import sys
input = sys.stdin.readline

def Kaprekar(n, cnt):
    if len(n) == 1:
        n = '000' + n
    elif len(n) == 2:
        n = '00' + n
    elif len(n) == 3:
        n = '0' + n
    if n == '6174':
        return cnt
    else:
        cnt += 1
        temp = sorted([num for num in n])
        res = temp[3] + temp[2] + temp[1] + temp[0]
        return Kaprekar(str(int(res)-int(res[::-1])), cnt)

t = int(input())
for _ in range(t):
    n = str(input().strip())
    print(Kaprekar(n, 0))