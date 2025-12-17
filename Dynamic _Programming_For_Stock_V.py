class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        
        # Initialize DP arrays
        # closed[j] stores the max profit after completing j transactions
        # hold_norm[j] stores max profit after starting j-th transaction as Normal (Buy)
        # hold_short[j] stores max profit after starting j-th transaction as Short (Sell)
        
        # We use -inf for impossible states to ensure max() logic works correctly
        inf = float('inf')
        closed = [0] * (k + 1)
        hold_norm = [-inf] * (k + 1)
        hold_short = [-inf] * (k + 1)
        
        for p in prices:
            # We use temporary lists for the current day's updates to ensure we 
            # strictly follow the "cannot start on same day as end" constraint.
            # All calculations for day 'i' use values from 'i-1' (stored in closed/hold_norm/hold_short).
            curr_closed = list(closed)
            curr_norm = list(hold_norm)
            curr_short = list(hold_short)
            
            for i in range(1, k + 1):
                # 1. Attempt to Start Transaction i
                
                # Start Normal: We had closed i-1 transactions, now we Buy (subtract price)
                curr_norm[i] = max(hold_norm[i], closed[i-1] - p)
                
                # Start Short: We had closed i-1 transactions, now we Sell (add price)
                curr_short[i] = max(hold_short[i], closed[i-1] + p)
                
                # 2. Attempt to End Transaction i
                
                # End Normal: We were holding normal (Bought), now we Sell (add price)
                # End Short: We were holding short (Sold), now we Buy back (subtract price)
                curr_closed[i] = max(closed[i], hold_norm[i] + p, hold_short[i] - p)
            
            # Update state for the next day
            closed = curr_closed
            hold_norm = curr_norm
            hold_short = curr_short
            
        # The result is the max profit found in any of the closed states.
        return max(closed)
