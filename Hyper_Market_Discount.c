#include <stdio.h>

int main() {
    double B, final_amount;

    // Read the bill amount B
    if (scanf("%lf", &B) != 1) return 0;

    // Apply 10% discount if B is greater than 2000
    if (B > 2000) {
        final_amount = B * 0.90;
    } else {
        final_amount = B;
    }

    // Print the final amount
    // Using %g helps print the number neatly without trailing zeros
    printf("%g\n", final_amount);

    return 0;
}
