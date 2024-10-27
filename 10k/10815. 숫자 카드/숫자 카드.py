n = int(input())
N = set(list(map(int, input().split())))
m = int(input())
M = list(map(int, input().split()))

for ele in M:
    if ele in N:
        print(1, end=" ")
    else:
        print(0, end=" ")