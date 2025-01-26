from collections import defaultdict
import sys
input = sys.stdin.readline

F = defaultdict(list)
n = int(input())
for _ in range(n):
    file, ex = input().rstrip().split('.')
    F[ex].append(file)

F = sorted(F.items())
for f in F:
    print(f[0], len(f[1]))