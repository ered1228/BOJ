#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    b = (a-b > b) ? a-b : b;
    c = (a-c > c) ? a-c : c;
    printf("%d", b*c*4);
    
    return 0;
}