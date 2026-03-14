class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Step 1: Check if k is valid
        total_happy_strings = 3 * (2 ** (n - 1))
        if k > total_happy_strings:
            return ""
        
        # 0-index k to make the division/modulo math perfectly align
        k -= 1 
        
        result = []
        choices = ['a', 'b', 'c']
        
        # Step 2: Determine the first character
        block_size = 2 ** (n - 1)
        idx = k // block_size
        result.append(choices[idx])
        
        # Update k to reflect the position within the chosen block
        k %= block_size 
        
        # Step 3: Determine the remaining n-1 characters
        for i in range(1, n):
            # The block size halves with each subsequent character
            block_size = 2 ** (n - 1 - i)
            
            # The available choices are the two letters not equal to the previous one,
            # checked in alphabetical order to maintain lexicographical sorting.
            available_choices = [c for c in ['a', 'b', 'c'] if c != result[-1]]
            
            idx = k // block_size
            result.append(available_choices[idx])
            
            k %= block_size
            
        return "".join(result)
