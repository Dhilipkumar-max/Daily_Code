#include <stdio.h>

int main() {
    long long M, B;

    // Read the remaining money M and number of beggars B
    if (scanf("%lld", &M) != 1) return 0;
    if (scanf("%lld", &B) != 1) return 0;

    // Calculate initial amount: M * 2^B
    // Using the bitwise left shift (1 << B) is an efficient way to calculate 2^B
    long long initial_money = M << B;

    // Print the result
    printf("%lld\n", initial_money);

    return 0;
}
