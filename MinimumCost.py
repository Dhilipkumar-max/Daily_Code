from sortedcontainers import SortedList

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        # We need to pick nums[0] and then (k-1) elements from a 
        # window of size (dist + 1).
        target = k - 1
        
        # 'left' keeps the smallest 'target' elements
        left = SortedList()
        # 'right' keeps the rest of the elements in the window
        right = SortedList()
        
        current_sum = 0
        
        # Helper to add an element to our two-set system
        def add(val):
            left.add(val)
            s_inc = val
            if len(left) > target:
                removed = left.pop() # Remove the largest from left
                right.add(removed)
                s_inc -= removed
            return s_inc

        # Helper to remove an element from our two-set system
        def remove(val):
            s_dec = 0
            if val in left:
                left.remove(val)
                s_dec = val
                if right:
                    added = right.pop(0) # Pull smallest from right to left
                    left.add(added)
                    s_dec -= added
            else:
                right.remove(val)
            return s_dec

        # Initial window: elements from index 1 to dist + 1
        for i in range(1, dist + 2):
            current_sum += add(nums[i])
            
        ans = current_sum
        
        # Slide the window across the rest of the array
        for i in range(dist + 2, n):
            # Remove the element that is falling out of the window
            current_sum -= remove(nums[i - dist - 1])
            # Add the new element
            current_sum += add(nums[i])
            ans = min(ans, current_sum)
            
        return nums[0] + ans
