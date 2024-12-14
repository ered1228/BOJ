from math import pi
x1,y1,x2,y2,x3,y3=map(int,input().split())
cx,cy=(x1+x2+x3)/3,(y1+y2+y3)/3
area=0.5*abs((x1*y2)+(x2*y3)+(x3*y1)-(x2*y1)-(x3*y2)-(x1*y3))
print(2*pi*cy*area,2*pi*cx*area)