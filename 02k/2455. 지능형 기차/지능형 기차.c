#include <stdio.h>

int main() {
    int a, b;
    int max = 0;
    int sum = 0;
    for (int i = 1; i < 5 ; i++) {
        scanf("%d %d", &a, &b);
        sum += (b - a);
        if (max < sum) max = sum;
    }
    printf("%d", max);
    
    return 0;
}