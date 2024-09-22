#include <stdio.h>
int main()
{    
    int n;
    scanf("%d", &n);
    
    int input;
    long long max = 0;
    long long min = 1000001;
    
    for(int i; i < n; i++)
    {
        scanf("%d", &input);
        if (input > max)
            max = input;
        if (input < min)
            min = input;
    }
    
    printf("%lld", max*min);
    return 0;
}