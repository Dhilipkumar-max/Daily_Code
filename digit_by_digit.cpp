#include <iostream>

using namespace std;

int main() {
    int N;
    if (cin >> N) {
        int sum = 0;
        while (N > 0) {
            int digit = N % 10;
            if (digit % 2 != 0) {
                sum += digit;
            }
            N /= 10;
        }
        
        cout << sum << endl;
    }
    return 0;
}
