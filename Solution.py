class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The first element is mandatory
        first_cost = nums[0]
        
        # We need to pick two more starting elements from the rest of the array
        # to minimize the sum, we pick the two smallest available.
        rest = sorted(nums[1:])
        
        return first_cost + rest[0] + rest[1]
