import bisect

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # 1. Sort events based on start time
        events.sort()
        n = len(events)
        
        # 2. Create a suffix max array
        # suffix_max[i] stores the maximum value from events[i...n-1]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i + 1])
        
        max_sum = 0
        
        # 3. Iterate through each event and find the best partner
        for i in range(n):
            start, end, val = events[i]
            
            # Case A: Only picking this single event
            max_sum = max(max_sum, val)
            
            # Case B: Picking this event and the best available event that starts AFTER this one ends
            # We need events[j].start > end
            # Use binary search to find the index of the first event with start > end
            idx = bisect.bisect_right(events, [end, float('inf'), float('inf')])
            
            if idx < n:
                max_sum = max(max_sum, val + suffix_max[idx])
                
        return max_sum
