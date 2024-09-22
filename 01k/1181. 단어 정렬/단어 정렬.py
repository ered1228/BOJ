n = int(input())
st = []
for i in range(n):
    st.append(input())
st2 = list(set(st))
st2.sort()
st2.sort(key = len)

for j in st2:
    print(j)