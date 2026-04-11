class Solution(object):
    def minimumDistance(self, nums):
        from collections import defaultdict
        indices_map = defaultdict(list)
        for index, val in enumerate(nums):
            indices_map[val].append(index)
            
        min_dist = float('inf')
        found = False
        
        for val in indices_map:
            indices = indices_map[val]
            if len(indices) >= 3:
                found = True
                for m in range(len(indices) - 2):
                    current_dist = 2 * (indices[m + 2] - indices[m])
                    if current_dist < min_dist:
                        min_dist = current_dist
                        
        return min_dist if found else -1
