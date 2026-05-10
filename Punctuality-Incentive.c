#include <stdio.h>

int main() {
    int I, N;
    long total_p = 0;

    // Read the initial incentive and number of days
    if (scanf("%d", &I) != 1) return 0;
    if (scanf("%d", &N) != 1) return 0;

    // Calculate total using the formula: P = (N/2) * (2*I + (N-1)*200)
    // Or use a simple loop
    for (int i = 0; i < N; i++) {
        total_p += (I + (i * 200));
    }

    // Print the output
    printf("%ld\n", total_p);

    return 0;
}
