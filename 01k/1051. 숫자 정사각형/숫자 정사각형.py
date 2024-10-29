def find_size(A, size, n, m):  
    R = []
    for i in range(n-size+1):
        for j in range(m-size+1):
            square = [A[i][j], A[i][j+size-1], A[i+size-1][j], A[i+size-1][j+size-1]]
            square = set(square)
            if len(square) == 1:
                R.append(size)
    if len(R) > 0:
        return size
    else:
        return find_size(A, size-1, n, m)

n, m = map(int, input().split())
A = []
for _ in range(n):
    row = str(input())
    A.append(row)

size = min(n, m)
print(find_size(A, size, n, m)**2)