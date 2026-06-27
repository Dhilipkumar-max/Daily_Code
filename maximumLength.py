from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        counts = Counter(nums)
        ans = 1
        
        # 1 is a special case because 1^2 = 1
        if 1 in counts:
            c1 = counts[1]
            ans = max(ans, c1 if c1 % 2 != 0 else c1 - 1)
            
        for k in counts:
            # Skip 1, as it is handled separately
            if k == 1:
                continue
                
            # Only start a chain if we can put the number on both sides of the pattern
            if counts[k] >= 2:
                length = 0
                curr = k
                
                # Keep growing the chain while we have at least 2 occurrences
                while counts[curr] >= 2:
                    length += 2
                    curr = curr * curr
                
                # If we have exactly 1 occurrence of the next squared value, it becomes the peak
                if counts[curr] == 1:
                    length += 1
                # If we don't have it at all, the previous value must be the peak instead
                else:
                    length -= 1
                    
                ans = max(ans, length)
                
        return ans
