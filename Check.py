class Solution(object):
    def check(self, nums):
        count_drops = 0
        n = len(nums)
        
        for i in range(n):
            # Use modulo to cleanly wrap around to the first element at the end
            if nums[i] > nums[(i + 1) % n]:
                count_drops += 1
                
            # Optimization: if we see more than 1 drop, we can fail early
            if count_drops > 1:
                return False
                
        return True
