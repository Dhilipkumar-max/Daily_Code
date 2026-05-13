class Solution(object):
    def minMoves(self, nums, limit):
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            l, r = min(a, b) + 1, max(a, b) + limit
            sum_val = a + b
            
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # Target range [l, r] requires only 1 move (subtract 1 from the 2)
            diff[l] -= 1
            diff[r + 1] += 1
            
            # Target sum_val requires 0 moves (subtract another 1 from the 1)
            diff[sum_val] -= 1
            diff[sum_val + 1] += 1
            
        # Sweep line to find the minimum moves
        ans = n
        current_moves = 0
        for i in range(2, 2 * limit + 1):
            current_moves += diff[i]
            ans = min(ans, current_moves)
            
        return ans
