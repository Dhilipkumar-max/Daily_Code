import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        def can_reduce_in_time(time_limit):
            total_reduced = 0
            for w in workerTimes:
                # Calculate the max height this worker can reduce within time_limit
                # Using the quadratic formula derived from: w * x(x+1) / 2 <= time_limit
                v = (2 * time_limit) // w
                
                # math.isqrt is computationally faster and avoids floating point inaccuracies
                x = (math.isqrt(1 + 4 * v) - 1) // 2
                total_reduced += x
                
                # Early exit if we already reached the required height
                if total_reduced >= mountainHeight:
                    return True
            return total_reduced >= mountainHeight

        # Binary search space for the time in seconds
        left = 0
        # The worst-case upper bound is if the fastest worker does all the work alone
        fastest_worker = min(workerTimes)
        right = fastest_worker * mountainHeight * (mountainHeight + 1) // 2
        
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_reduce_in_time(mid):
                ans = mid       # This time is possible, save it
                right = mid - 1 # Try to find a smaller time
            else:
                left = mid + 1  # Time is too small, we need more time
                
        return ans
