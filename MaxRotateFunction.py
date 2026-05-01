class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
            
        array_sum = sum(nums)
        
        # Calculate F(0)
        current_f = sum(i * num for i, num in enumerate(nums))
        max_f = current_f
        
        # Calculate F(k) for k = 1 to n-1 using the recurrence relation
        for k in range(1, n):
            # The element that moves from the end of the current rotation to the front
            # is at index n - k in the original array
            current_f = current_f + array_sum - (n * nums[n - k])
            
            # Update the maximum value found so far
            if current_f > max_f:
                max_f = current_f
                
        return max_f
