n = int(input())
for i in range(n):
    s = list(map(int, input().split()))
    print(f"Case #{i+1}: {max(s)}")