class Solution {
    public int concatenatedBinary(int n) {
        long res = 0;
        int MOD = 1_000_000_007;
        int bitLength = 0;

        for (int i = 1; i <= n; i++) {
            // Check if i is a power of 2 to increment bitLength
            // e.g., 1 (1), 2 (10), 4 (100), 8 (1000)...
            if ((i & (i - 1)) == 0) {
                bitLength++;
            }

            // (res << bitLength) makes room for the new bits
            // | i adds the binary representation of i to the end
            res = ((res << bitLength) | i) % MOD;
        }

        return (int) res;
    }
}
