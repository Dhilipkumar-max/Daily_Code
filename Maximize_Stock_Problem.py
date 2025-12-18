class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        initial_profit = 0
        for p, s in zip(prices, strategy):
            initial_profit += p * s
        
        # Calculate the gain for the very first window [0, k-1]
        half_k = k // 2
        current_gain = 0
        
        # First half of the window: strategy becomes 0
        for i in range(half_k):
            current_gain += (0 - strategy[i]) * prices[i]
            
        # Second half of the window: strategy becomes 1
        for i in range(half_k, k):
            current_gain += (1 - strategy[i]) * prices[i]
            
        max_gain = current_gain
        
        # Slide the window from left to right
        # i is the start of the window
        for i in range(1, n - k + 1):
            # Element leaving the first half
            old_first_half_start = i - 1
            current_gain -= (0 - strategy[old_first_half_start]) * prices[old_first_half_start]
            
            # Element moving from second half to first half
            # This is the element at index (i + half_k - 1)
            mid_idx = i + half_k - 1
            current_gain -= (1 - strategy[mid_idx]) * prices[mid_idx] # remove from 2nd half logic
            current_gain += (0 - strategy[mid_idx]) * prices[mid_idx] # add to 1st half logic
            
            # Element entering the second half
            new_second_half_end = i + k - 1
            current_gain += (1 - strategy[new_second_half_end]) * prices[new_second_half_end]
            
            if current_gain > max_gain:
                max_gain = current_gain
                
        # We can also choose not to modify, but since k elements MUST be selected 
        # for modification per instructions ("Selecting exactly k..."), 
        # we check if max_gain helps the initial profit.
        return initial_profit + max(0, max_gain)
