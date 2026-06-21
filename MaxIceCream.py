class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        # Find the maximum cost to know the size of our counting array
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        
        # Populate the frequency array
        for cost in costs:
            freq[cost] += 1
            
        ice_creams_bought = 0
        
        # Iterate through prices in increasing order
        for price in range(1, max_cost + 1):
            if freq[price] > 0:
                # Calculate how many of this price we can afford
                can_buy = min(freq[price], coins // price)
                
                # Update coins and count
                coins -= (can_buy * price)
                ice_creams_bought += can_buy
                
                # If we can't afford any more of this price, we are done
                if coins < price:
                    break
                    
        return ice_creams_bought
