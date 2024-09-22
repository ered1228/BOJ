#include <stdio.h>
int main()
{
    char alphabet;
    scanf("%c", &alphabet);
    
    if (alphabet == 'N' || alphabet == 'n')
        printf("Naver D2");
    else
        printf("Naver Whale");
    
    return 0;
}