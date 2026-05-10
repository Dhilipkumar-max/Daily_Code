#include <stdio.h>

int main() {
    long M, N;

    // Read values for M and N
    if (scanf("%ld %ld", &M, &N) != 2) return 0;

    // A number is divisible if the remainder is 0
    if (M % N == 0) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
