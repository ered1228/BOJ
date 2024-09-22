#include <stdio.h>
#include <stdbool.h>

#define MOD 4294967296

bool A[100000001];
int main(){
    int i, j;
    for (i = 2; i < 10000; i++)
        if (!A[i])
            for (j = 2*i; j < 100000001; j += i)
                A[j] = true; //false가 소수
				
    int n;
    scanf("%d", &n);
    long long res = 1;
    for (i = 2; i < 100000001; i++)
        if (!A[i]){
            long long temp = 1;
            while (temp * i <= n) temp *= i;
            res = (res * temp) % MOD;
        }
    printf("%lld", res);
}