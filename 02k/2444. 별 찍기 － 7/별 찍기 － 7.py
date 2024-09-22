n = int(input())
for i in range(1, n):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))
print("*"*(2*n-1))
for j in range(1, n):
    print(" "*j, end="")
    print("*"*(2*(n-j)-1))