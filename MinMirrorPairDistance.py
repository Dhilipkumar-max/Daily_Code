class Solution(object):
    def minMirrorPairDistance(self, nums):
        seen = {}
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            # Check if the current number is a reversed version of a previously seen number
            if num in seen:
                min_dist = min(min_dist, j - seen[num])
            
            rev_num = int(str(num)[::-1])
            
            seen[rev_num] = j
            
        return min_dist if min_dist != float('inf') else -1
