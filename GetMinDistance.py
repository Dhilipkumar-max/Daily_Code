class Solution(object):
    def getMinDistance(self, nums, target, start):
        
        min_dist = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                current_dist = abs(i - start)
                if current_dist < min_dist:
                    min_dist = current_dist
                    
                if min_dist == 0:
                    return 0
        
        return min_dist
