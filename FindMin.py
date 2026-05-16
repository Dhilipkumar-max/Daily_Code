class Solution(object):
    def findMin(self, nums):
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # The minimum element must be in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # The minimum element is at mid or in the left half
                right = mid
            else:
                # nums[mid] == nums[right]
                # We can't decide the direction, so safely shrink the right bound
                right -= 1
                
        return nums[left]
        
