class Solution(object):
    def isGood(self, nums):
        # The expected maximum value n is always length - 1
        n = len(nums) - 1
        
        # base[1] is the smallest valid case [1, 1], length must be at least 2
        if n < 1:
            return False
        
        nums.sort()
        
        # Check if the first n-1 elements are 1, 2, ..., n-1
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        
        # Check if the last two elements are both n
        return nums[n-1] == n and nums[n] == n
