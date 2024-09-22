import sys
input = sys.stdin.readline
st = []

k = int(input())

for i in range(k):
    c = int(input())
    if c != 0:
        st.append(c)
    else:
        st.pop()

print(sum(st))