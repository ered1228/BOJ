x = int(input())

for i in range(1, 5000):
    if (x > (i*(i-1))//2) and ((((i+1)*i)//2) >= x):
        i_list = i #i번째 줄
        n = x - (i*(i-1))//2 #n번째 수

if (i_list)%2 == 0:
    s = n
    m = (i_list + 1) - n
elif (i_list)%2 != 0:
    s = (i_list + 1) - n
    m = n
print("{}/{}".format(s, m))