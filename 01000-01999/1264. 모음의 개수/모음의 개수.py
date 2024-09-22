while True:
    st = str(input())
    res = 0
    if st == '#':
        break
    else:
        st = st.lower()
        res = st.count('a') + st.count('e') + st.count('i') + st.count('o') + st.count('u')
        print(res)