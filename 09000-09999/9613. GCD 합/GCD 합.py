import math

def sumgcd(nums):
    l = nums[0]
    G = []
    nums = nums[1:]
    for i in range(l):
        for j in range(i+1, l):
            G.append(math.gcd(nums[i], nums[j]))
    return sum(G)

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    print(sumgcd(nums))