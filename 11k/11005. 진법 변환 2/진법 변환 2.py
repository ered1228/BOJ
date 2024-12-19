n, b = map(int, input().split())
res = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while n:
    res += str(arr[n%b])
    n //= b

print(res[::-1])