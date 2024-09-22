import math

n = int(input())
nums = list(map(int, input().split()))
a = 0 # 합성수의 개수 

for i in nums:
    if i == 1:
        a += 1
    else:
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                a += 1
                break
print(n - a)