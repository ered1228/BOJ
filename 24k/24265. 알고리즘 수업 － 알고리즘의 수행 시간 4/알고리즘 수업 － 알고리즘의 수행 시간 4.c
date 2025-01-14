#include <stdio.h>
int main() {
    long long n;
    long long sum = 0;
    scanf("%lld", &n);
    if (n == 1) {
        printf("%d\n", 0);
        printf("%d", 2);
    } else {
        for (int i = 1; i < n; i++)
            sum = sum + i;
        printf("%lld\n", sum);
        printf("%d", 2);
    }
    return 0;
}