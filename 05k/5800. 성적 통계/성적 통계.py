import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    A = list(map(int, input().split()))
    s = A[0]
    A.remove(A[0])
    A.sort()
    print("Class {}".format(i+1))
    B = [A[j+1] - A[j] for j in range(0, s-1)]
    print("Max {0}, Min {1}, Largest gap {2}".format(A[s-1], A[0], max(B)))