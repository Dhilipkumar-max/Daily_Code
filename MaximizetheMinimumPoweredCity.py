class Solution(object):
    def maxPower(self, stations, r, k):
        n = len(stations)
        
        # Step 1: Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        
        # Function to get total power available to city i
        def get_power(i):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            return prefix[right + 1] - prefix[left]

        # Step 2: Initialize power[] for all cities
        power = [get_power(i) for i in range(n)]
        
        # Step 3: Feasibility check
        def can(mid):
            added = 0
            add = [0] * (n + 1)
            curr_add = 0
            
            for i in range(n):
                curr_add += add[i]
                if power[i] + curr_add < mid:
                    need = mid - (power[i] + curr_add)
                    added += need
                    if added > k:
                        return False
                    curr_add += need
                    if i + 2 * r + 1 < n:
                        add[i + 2 * r + 1] -= need
            return True
        
        # Step 4: Binary search
        low, high = 0, sum(stations) + k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
