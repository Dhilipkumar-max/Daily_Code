class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        from collections import defaultdict
        
        left = defaultdict(int)
        right = defaultdict(int)
        
        for x in nums:
            right[x] += 1
        
        ans = 0
        
        for j in range(len(nums)):
            right[nums[j]] -= 1
            target = nums[j] * 2
            
            count_before = left[target]
            count_after = right[target]
            
            ans = (ans + count_before * count_after) % MOD
            
            left[nums[j]] += 1
        
        return ans
