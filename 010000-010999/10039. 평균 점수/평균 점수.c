#include <stdio.h>
int main()
{
    int sum = 0;
    int temp;
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &temp);
        if (temp < 40)
            temp = 40;
        sum += temp;
    }
    printf("%d", sum/5);
    return 0;
}