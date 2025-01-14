from collections import deque
import sys
input = sys.stdin.read
output = sys.stdout.write

def BFS(A, B):
    queue = deque([A])
    visited = {A: None}    
    while queue:
        val = queue.popleft()
        if val == B:
            break

        d = (2 * val) % 10000
        if d not in visited:
            visited[d] = (val, 'D')
            queue.append(d)
        
        s = 9999 if val == 0 else val - 1
        if s not in visited:
            visited[s] = (val, 'S')
            queue.append(s)
        
        l = (val % 1000) * 10 + val // 1000
        if l not in visited:
            visited[l] = (val, 'L')
            queue.append(l)
        
        r = (val % 10) * 1000 + val // 10
        if r not in visited:
            visited[r] = (val, 'R')
            queue.append(r)

    operations = []
    while B != A:
        prev, op = visited[B]
        operations.append(op)
        B = prev
    return ''.join(reversed(operations))

def main():
    data = input().splitlines()
    t = int(data[0])
    results = []    
    for i in range(1, t+1):
        A, B = map(int, data[i].split())
        results.append(BFS(A, B))
    
    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()