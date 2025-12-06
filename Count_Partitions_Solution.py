class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp[i] = #ways to partition first i elements (nums[0..i-1])
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)  # prefix[i] = sum(dp[0..i]) % MOD
        
        dp[0] = 1
        prefix[0] = 1
        
        min_d = deque()  # increasing deque of indices for min
        max_d = deque()  # decreasing deque of indices for max
        
        l = 0  # left boundary of the valid window
        
        for r in range(n):
            # Insert nums[r] into min_d (maintain increasing order)
            while min_d and nums[min_d[-1]] >= nums[r]:
                min_d.pop()
            min_d.append(r)
            
            # Insert nums[r] into max_d (maintain decreasing order)
            while max_d and nums[max_d[-1]] <= nums[r]:
                max_d.pop()
            max_d.append(r)
            
            # Shrink from the left until window [l..r] satisfies max - min <= k
            while nums[max_d[0]] - nums[min_d[0]] > k:
                if min_d[0] == l:
                    min_d.popleft()
                if max_d[0] == l:
                    max_d.popleft()
                l += 1
            
            # Now any start in [l..r] yields a valid segment [start..r]
            # dp index matches start (since dp[x] = ways for first x elements)
            if l == 0:
                dp[r + 1] = prefix[r] % MOD  # sum(dp[0..r])
            else:
                dp[r + 1] = (prefix[r] - prefix[l - 1]) % MOD  # sum(dp[l..r])
            
            prefix[r + 1] = (prefix[r] + dp[r + 1]) % MOD
        
        return dp[n] % MOD
