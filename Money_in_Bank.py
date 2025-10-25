class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7
        
        # Money saved in complete weeks
        # Week 1: 28, Week 2: 35, Week 3: 42 ...
        # Each week adds 7 more than previous
        total = 7 * (weeks * (weeks - 1) // 2) + 28 * weeks
        
        # Money in the remaining days of the last partial week
        start = weeks + 1
        for i in range(days):
            total += start + i
        
        return total
