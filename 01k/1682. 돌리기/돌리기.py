from collections import deque

def BFS(I, S):
    queue = deque([(I, 0)])
    cnt = 0
    v = set(tuple(I))
    while queue:
        arr, cnt = queue.popleft()
        if arr == S:
            return cnt
        if tuple(arr) not in v:
            v.add(tuple(arr))
            for n_arr in next_arr(arr):
                if tuple(n_arr) not in v:
                    queue.append((n_arr, cnt+1))
    return -1
                
def next_arr(arr):
    A = arr[::-1]
    temp1 = deque(arr[:4]) ; temp2 = deque(arr[4:])
    temp1.appendleft(temp1.pop()) ; temp2.append(temp2.popleft())
    B = list(temp1) + list(temp2)
    C = [arr[0], arr[2], arr[5], arr[3], arr[4], arr[6], arr[1], arr[7]]
    D = [arr[4], arr[1], arr[2], arr[3], arr[0], arr[5], arr[6], arr[7]]
    return [A, B, C, D]

I = [1, 2, 3, 4, 5, 6, 7, 8]
S = list(map(int, input().split()))
print(BFS(I, S))