lena = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = str(input())
for a in lena:
    s = s.replace(a, '1')
print(len(s))