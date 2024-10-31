from collections import deque

def find(n, m, A):
    if n == 1:
        return 1
    elif n == 2:
        if m == 0 and A[0] >= A[1]:
            return 1
        elif m == 0 and A[0] < A[1]:
            return 2
        elif m == 1 and A[0] >= A[1]:
            return 2
        else:
            return 1
    else:
        B = deque([ele for ele in enumerate(A)])
        A.sort(reverse=True)
        C = deque(A)
        cnt = 0
        while True:
            if C[0] == B[0][1]:
                inx = B[0][0]
                B.popleft()
                cnt += 1
                C.popleft()
                if inx == m:
                    break
            else:
                B.append(B.popleft())
    return cnt

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    print(find(n, m, A))