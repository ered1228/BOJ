import sys
input = sys.stdin.readline

m, n = map(int, input().split()) #m은 숫자 수, n은 테스트 케이스
nums = list(map(int, input().split())) #수열
sp = [0]
temp = 0

for i in range(m):
    temp += nums[i]
    sp.append(temp)

for _ in range(n):
    i, j = map(int, input().split())
    result = sp[j] - sp[i-1]
    print(result)