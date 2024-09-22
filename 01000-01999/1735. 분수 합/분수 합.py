def Eu(a, b):
    if b == 0:
        return a
    else:
        return Eu(b, a%b)

a, b = map(int, input().split()) #a/b
c, d = map(int, input().split()) #c/d

ra = (a * d) + (b * c)
rb = b * d
gcd = Eu(ra, rb)

ra = ra // gcd
rb = rb // gcd
print(ra, rb)