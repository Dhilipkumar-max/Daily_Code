class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Set of primes up to 20 (since 2^20 > 10^6)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        
        for num in range(left, right + 1):
            # bin(num).count('1') counts the set bits
            # Alternatively, in Python 3.10+, you can use num.bit_count()
            if bin(num).count('1') in primes:
                count += 1
                
        return count
