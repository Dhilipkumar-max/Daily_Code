class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total = sum(batteries)
        
        # Search space for answer: [0, total // n]
        lo, hi = 0, total // n
        
        def can_run(T):
            # Total contribution towards T minutes
            usable = 0
            for b in batteries:
                usable += min(b, T)
                # Small optimization: early exit if already enough
                if usable >= n * T:
                    return True
            return usable >= n * T
        
        while lo < hi:
            mid = (lo + hi + 1) // 2  # upper mid to avoid infinite loop
            if can_run(mid):
                lo = mid
            else:
                hi = mid - 1
        
        return lo
