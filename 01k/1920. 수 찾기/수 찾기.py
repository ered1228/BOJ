import sys
input = sys.stdin.readline

def binary_s(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0
 
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
tests = list(map(int, input().split()))
nums.sort()

for i in range(m):
    result = binary_s(nums, tests[i], 0, n-1)
    print(result)