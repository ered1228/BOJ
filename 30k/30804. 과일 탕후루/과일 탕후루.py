from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
start, end = 0, 0
temp_dict = defaultdict(int)
l = 1
while end < n:
    temp_dict[A[end]] += 1
    if len(temp_dict) > 2:
        temp_dict[A[start]] -= 1
        if temp_dict[A[start]] < 1:
            del temp_dict[A[start]]
        start += 1
    l = max(l, end-start+1)
    end += 1
print(l)