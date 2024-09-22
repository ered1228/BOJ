from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
tests = list(map(int, input().split()))
cards.sort()

for t in tests:
    result = bisect_right(cards, t) - bisect_left(cards, t)
    print(result, end=" ")