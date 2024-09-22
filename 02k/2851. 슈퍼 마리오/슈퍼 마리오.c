#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[11] = {0};
    int a;
    for (int i = 1; i < 11; i++) {
        scanf("%d", &a);
        arr[i] = arr[i-1] + a;
    }
    if (arr[10] < 100) {
        printf("%d", arr[10]);
    } else {
        for (int j = 0; j < 11; j++) {
                if (arr[j] == 100) {
                    printf("%d", 100);
                    break;
                } else if (arr[j] > 100) {
                    if (abs(arr[j-1] - 100) >= abs(arr[j] - 100))
                    printf("%d", arr[j]);
                    else if (abs(arr[j-1] - 100) < abs(arr[j] - 100))
                    printf("%d", arr[j-1]);
                    break;   
                }
        }
    }
    return 0;
}