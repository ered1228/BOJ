import sys
input = sys.stdin.readline

def VPS(parentheses):
    st = []
    for p in parentheses:
        if p == '(':
            st.append(p)
        else:
            if len(st) != 0:
                st.pop()
            else:
                return False
    if len(st) == 0:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    parentheses = str(input().strip())
    if VPS(parentheses):
        print("YES")
    else:
        print("NO")