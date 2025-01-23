from collections import defaultdict

n = int(input())
toxic = list(map(int, input().split()))
gar = defaultdict(int)
for t in toxic:
    gar[t] += 1

print(len(gar))