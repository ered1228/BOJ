#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int area = a * b;
    if ((area % 24200) == 0) {
        printf("%d", area / 24200);
    } else {
        printf("%d", (area/24200)+1); }
    
    return 0;
}