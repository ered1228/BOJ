// 세 각의 크기가 모두 60이면, Equilateral
//세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
//세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
//세 각의 합이 180이 아닌 경우에는 Error
#include <stdio.h>
int main()
{
    int sum = 0;
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    sum = a + b + c;
    
    if (sum != 180)
        printf("Error");
    else
        if (a == 60 && b == 60 && c == 60)
            printf("Equilateral");
        else if (a == b || b == c || a == c)
            printf("Isosceles");
        else
            printf("Scalene");

    return 0;
}