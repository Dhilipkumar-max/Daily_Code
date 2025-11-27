class Solution(object):
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        prefMin = [float('inf')] * k
        
        prefix = 0
        ans = float('-inf')
        
        # prefix sum before array starts = 0 (bucket 0)
        prefMin[0] = 0
        
        for i in range(n):
            prefix += nums[i]
            mod = (i + 1) % k
            
            if prefMin[mod] != float('inf'):
                ans = max(ans, prefix - prefMin[mod])
            
            prefMin[mod] = min(prefMin[mod], prefix)
        
        return ans
