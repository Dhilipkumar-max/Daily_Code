#include <stdio.h>

int main() {
    int H, M;
    long total_seconds;

    // Read the values of H and M
    if (scanf("%d", &H) != 1) return 0;
    if (scanf("%d", &M) != 1) return 0;

    // Calculate the total seconds
    // Using long to prevent overflow for large inputs
    total_seconds = (H * 3600L) + (M * 60L);

    // Print the output
    printf("%ld\n", total_seconds);

    return 0;
}
