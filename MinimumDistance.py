class Solution(object):
    def minimumDistance(self, nums):
        pos_map = {}
        for idx, val in enumerate(nums):
            if val not in pos_map:
                pos_map[val] = []
            pos_map[val].append(idx)
        
        min_dist = float('inf')
        found = False
        
        # Iterate through each number's list of indices
        for val in pos_map:
            indices = pos_map[val]
            # We need at least 3 indices to form a good tuple
            if len(indices) >= 3:
                found = True
                # Check every window of 3 consecutive indices for that number
                # Since the indices are added in increasing order, 
                # distance is minimized by choosing adjacent occurrences.
                for i in range(len(indices) - 2):
                    # Distance is 2 * (indices[k] - indices[i]) for i < j < k
                    dist = 2 * (indices[i + 2] - indices[i])
                    if dist < min_dist:
                        min_dist = dist
        
        return min_dist if found else -1
