class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        cur_penalty = 0
        min_penalty = 0
        best_hour = 0
        
        for i, char in enumerate(customers):
            # If we see a 'Y', keeping the shop open for this hour 
            # reduces the penalty relative to closing before this hour.
            if char == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            
            # If the current penalty is lower than our best seen so far,
            # update the best_hour.
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                best_hour = i + 1
                
        return best_hour
