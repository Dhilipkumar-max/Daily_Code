class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Convert binary string to decimal integer
        n = int(s, 2)
        steps = 0
        
        # Step 2: Loop until n is reduced to 1
        while n > 1:
            steps += 1
            # Step 3: Apply rules based on parity
            if n % 2 == 0:
                # Rule: Even -> divide by 2
                n = n // 2
            else:
                # Rule: Odd -> add 1
                n += 1
                
        return steps
