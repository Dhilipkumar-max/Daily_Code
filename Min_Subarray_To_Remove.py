class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        rem = total % p
        
        # If already divisible, no need to remove anything
        if rem == 0:
            return 0
        
        seen = {0: -1}  # prefix_mod -> index
        cur = 0
        n = len(nums)
        ans = n  # start with "worst" (remove entire array)
        
        for i, x in enumerate(nums):
            cur = (cur + x) % p
            target = (cur - rem) % p  # we want a previous prefix with this mod
            
            if target in seen:
                ans = min(ans, i - seen[target])
            
            # Store latest index for this remainder (helps get shorter subarrays later)
            seen[cur] = i
        
        # If we ended up needing to remove the whole array, it's not allowed
        return ans if ans < n else -1
