#include <stdio.h>

int main() {
    int x_bl, y_bl, side;

    // Read the x, y coordinates and the side length
    if (scanf("%d", &x_bl) != 1) return 0;
    if (scanf("%d", &y_bl) != 1) return 0;
    if (scanf("%d", &side) != 1) return 0;

    // Calculate and print top right coordinates
    printf("%d\n", x_bl + side);
    printf("%d\n", y_bl + side);

    return 0;
}
