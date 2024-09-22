import sys
input = sys.stdin.readline

n = int(input())
temp = 0
for i in range(n):
    a = int(input())
    temp += a
print(temp-(n-1))