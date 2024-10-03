n = int(input())
nums = list(map(int, input().split()))
odd, even = 0, 0
for a in nums:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

if n % 2 == 0:
    if even == odd:
        print(1)
    else:
        print(0)
else:
    if even + 1 == odd:
        print(1)
    else:
        print(0)