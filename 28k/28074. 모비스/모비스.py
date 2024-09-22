s = str(input())
A = [0]*5
A[0] = s.count('M')
A[1] = s.count('O')
A[2] = s.count('B')
A[3] = s.count('I')
A[4] = s.count('S')
if A[0] > 0 and A[1] > 0 and A[2] > 0 and A[3] > 0 and A[4] > 0:
    print("YES")
else:
    print("NO")