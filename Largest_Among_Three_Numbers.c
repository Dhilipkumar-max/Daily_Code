#include <stdio.h>

int main() {
    long A, B, C;

    // Read the three integers
    if (scanf("%ld %ld %ld", &A, &B, &C) != 3) return 0;

    // Compare to find the largest value
    if (A >= B && A >= C) {
        printf("%ld\n", A);
    } else if (B >= A && B >= C) {
        printf("%ld\n", B);
    } else {
        printf("%ld\n", C);
    }

    return 0;
}
