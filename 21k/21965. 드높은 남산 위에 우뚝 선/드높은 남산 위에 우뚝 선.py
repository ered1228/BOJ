import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    result = 'YES'
else:
    if nums[0] == nums[1]:
        result = 'NO'
    elif nums[0] - nums[1] > 0: #계속 감소해야 산인 경우
        result = 'YES'
        for i in range(1, n-1):
            if nums[i] - nums[i+1] <= 0:
                result = 'NO'
                break
    else:
        m = nums.index(max(nums))
        a = nums.count(max(nums))
        if a != 1:
            result = 'NO'
        else:
            result = 'YES'
            for j in range(m, n-1):
                if nums[j] - nums[j+1] <= 0:
                    result = 'NO'
                    break
            for k in range(1, m):
                if nums[k] - nums[k+1] >= 0:
                    result = 'NO'
                    break
print(result)

# 1. 증가하다가 감소하는 경우
# max값 인덱스를 찾고, 그 인덱스가 유일함을 확인하고, 그 인덱스부터 감소함을 찾아야 함
# 2. 계속 증가해야 하는 경우
# max값 인덱스를 찾고, 그 인덱스가 n-1로 유일함을 확인해야 함.