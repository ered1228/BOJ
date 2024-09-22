import sys
input = sys.stdin.readline
cow = [[0] for _ in range(10)]

def find(arr):
    cnt = 0
    for i in range(1, len(arr)-1):
        if arr[i] != arr[i+1]:
            cnt += 1
    return cnt

n = int(input())
res = 0
for _ in range(n):
    a, b = map(int, input().split())
    cow[a-1].append(b)

for j in range(10):
    res += find(cow[j])

print(res)