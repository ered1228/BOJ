a = int(input())
b = int(input())
b_hun = b//100
b_ten = (b%100)//10
b_one = (b%10)
print((b_one)*a)
print((b_ten)*a)
print((b_hun)*a)
print(a*b)