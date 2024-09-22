n = int(input())
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
arr2 = [0]*28

arr.extend(arr2)
for i in range(18, 46):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr[n])