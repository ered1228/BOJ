n = int(input())
arr = [0]*91

arr[1] = 1
arr[2] = 1
for i in range(3, 91):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr[n])