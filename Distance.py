from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        # Group indices by their values
        groups = defaultdict(list)
        for i, val in enumerate(nums):
            groups[val].append(i)
            
        for val in groups:
            indices = groups[val]
            k = len(indices)
            if k <= 1:
                continue
            
            # Total sum of all indices for this value
            total_sum = sum(indices)
            prefix_sum = 0
            
            for i, idx in enumerate(indices):
                # Number of elements to the left: i
                # Number of elements to the right: k - 1 - i
                
                # Formula: (count_left * current_idx - sum_left) + (sum_right - count_right * current_idx)
                left_part = (i * idx) - prefix_sum
                
                # sum_right is (total_sum - prefix_sum - current_idx)
                right_sum = total_sum - prefix_sum - idx
                right_part = right_sum - (k - 1 - i) * idx
                
                res[idx] = left_part + right_part
                
                # Update prefix_sum for the next index in the group
                prefix_sum += idx
                
        return res
