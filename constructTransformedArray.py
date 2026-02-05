class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            # The target index is the current index + the jump, 
            # wrapped around the array size n.
            target_index = (i + nums[i]) % n
            result[i] = nums[target_index]
            
        return result
