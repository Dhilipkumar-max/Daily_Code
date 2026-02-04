class Solution(object):
    def maxSumTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return 0
        
        # 1. max_prefix[i]: Max sum of a strictly increasing subarray ending at i (length >= 2).
        # We use a Kadane-like approach restricted to strictly increasing elements.
        max_prefix = [float('-inf')] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # Option A: Just the pair [i-1, i]
                # Option B: Extend the best increasing subarray ending at i-1
                max_prefix[i] = max(nums[i] + nums[i-1], max_prefix[i-1] + nums[i])

        # 2. max_suffix[i]: Max sum of a strictly increasing subarray starting at i (length >= 2).
        max_suffix = [float('-inf')] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                # Option A: Just the pair [i, i+1]
                # Option B: Extend the best increasing subarray starting at i+1
                max_suffix[i] = max(nums[i] + nums[i+1], nums[i] + max_suffix[i+1])

        # 3. max_dec_prefix[i]: Max sum of a strictly decreasing subarray ending at i 
        # that started at some peak p, where p has a valid max_prefix[p].
        # This allows us to find the best (prefix + middle) in one pass.
        max_trionic = float('-inf')
        dp_dec = [float('-inf')] * n
        
        for i in range(1, n - 1):
            # If nums[i-1] > nums[i], we are in a decreasing slope.
            if nums[i] < nums[i-1]:
                # Potential peak at i-1
                if max_prefix[i-1] != float('-inf'):
                    dp_dec[i] = max(dp_dec[i], max_prefix[i-1] + nums[i])
                
                # Continue decreasing from dp_dec[i-1]
                if dp_dec[i-1] != float('-inf'):
                    dp_dec[i] = max(dp_dec[i], dp_dec[i-1] + nums[i])
            
            # If we have a valid prefix+decreasing part ending at i, 
            # and i can be the start of an increasing suffix:
            if dp_dec[i] != float('-inf') and max_suffix[i] != float('-inf'):
                # dp_dec[i] includes nums[i], max_suffix[i] includes nums[i].
                # Subtract nums[i] once to get the contiguous sum.
                max_trionic = max(max_trionic, dp_dec[i] + max_suffix[i] - nums[i])
                        
        return max_trionic
