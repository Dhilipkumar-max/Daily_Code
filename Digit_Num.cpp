#include <iostream>

using namespace std;

int main() {
    int N;
    if (cin >> N) {
        int sum = 0;
        
        // Loop runs until all digits are extracted and processed
        while (N > 0) {
            // Extract the last digit using modulo operator (%)
            int digit = N % 10;
            
            // Check if the digit is odd
            if (digit % 2 != 0) {
                sum += digit;
            }
            
            // Remove the last digit using integer division (/)
            N /= 10;
        }
        
        cout << sum << endl;
    }
    return 0;
}
