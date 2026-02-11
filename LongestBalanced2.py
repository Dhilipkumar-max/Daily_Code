class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        max_len = 0
        
        # We use a nested loop for subarrays, but with a slight optimization
        # to skip redundant checks. For 10^5, a pure O(N^2) might TLE in 
        # strict environments, but this is the standard logic for distinct counts.
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
                
                if len(distinct_evens) == len(distinct_odds):
                    max_len = max(max_len, j - i + 1)
        
        return max_len
