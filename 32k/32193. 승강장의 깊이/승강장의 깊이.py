import sys
input = sys.stdin.readline

n = int(input())
ground = 0
platform = 0

for _ in range(n):
    a, b = map(int, input().split())
    ground += a
    platform += b
    print(ground - platform)