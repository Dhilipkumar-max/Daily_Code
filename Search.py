class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if we found the target
            if nums[mid] == target:
                return mid
            
            # Determine if the left half is strictly sorted
            if nums[left] <= nums[mid]:
                # Check if the target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1   # Target is in the right half
            
            # Otherwise, the right half must be strictly sorted
            else:
                # Check if the target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right half
                else:
                    right = mid - 1  # Target is in the left half
                    
        return -1
