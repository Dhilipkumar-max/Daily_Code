class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        
        # If total sum is odd, no partition will have even difference
        if total % 2 == 1:
            return 0
        
        # If total sum is even, all n-1 partitions work
        return len(nums) - 1
