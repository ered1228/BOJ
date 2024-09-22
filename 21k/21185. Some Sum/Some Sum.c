#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    if (n % 4 == 0)
        printf("%s", "Even");
    else if (n % 2 == 0)
        printf("%s", "Odd");
    else
        printf("%s", "Either");
    
    return 0;

}