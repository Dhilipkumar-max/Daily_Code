class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ans tracks total valid substrings
        # prev tracks the length of the previous group of characters
        # cur tracks the length of the current group of characters
        ans = 0
        prev = 0
        cur = 1
        
        for i in range(1, len(s)):
            # If the character changes, the current group ends
            if s[i] != s[i-1]:
                # Add the number of valid substrings formed by the last two groups
                ans += min(prev, cur)
                # Move current group length to previous, reset current to 1
                prev = cur
                cur = 1
            else:
                # Still in the same group
                cur += 1
        
        # Add the result for the final two groups after the loop ends
        return ans + min(prev, cur)
