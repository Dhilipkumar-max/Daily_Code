import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or k == 0:
            return 0
            
        # 1. Build the Sparse Table for O(1) Range Maximum and Minimum Queries (RMQ)
        st_max = [list(nums)]
        st_min = [list(nums)]
        
        j = 1
        while (1 << j) <= n:
            prev_max = st_max[-1]
            prev_min = st_min[-1]
            
            # Length of the current row in the sparse table
            curr_length = n - (1 << j) + 1
            curr_max = [0] * curr_length
            curr_min = [0] * curr_length
            
            offset = 1 << (j - 1)
            for i in range(curr_length):
                curr_max[i] = prev_max[i] if prev_max[i] > prev_max[i + offset] else prev_max[i + offset]
                curr_min[i] = prev_min[i] if prev_min[i] < prev_min[i + offset] else prev_min[i + offset]
                
            st_max.append(curr_max)
            st_min.append(curr_min)
            j += 1
            
        # Precompute logarithms for fast sparse table access
        log2 = [0] * (n + 1)
        for i in range(2, n + 1):
            log2[i] = log2[i // 2] + 1
            
        def get_val(l, r):
            k_log = log2[r - l + 1]
            row_max = st_max[k_log]
            row_min = st_min[k_log]
            right_idx = r - (1 << k_log) + 1
            
            mx = row_max[l] if row_max[l] > row_max[right_idx] else row_max[right_idx]
            mn = row_min[l] if row_min[l] < row_min[right_idx] else row_min[right_idx]
            
            return mx - mn

        # 2. Max Heap to find the top k elements
        pq = []
        
        # Max heap in Python is simulated using negative numbers
        initial_val = get_val(0, n - 1)
        heapq.heappush(pq, (-initial_val, 0, n - 1))
        
        visited = {(0, n - 1)}
        ans = 0
        
        for _ in range(k):
            neg_val, l, r = heapq.heappop(pq)
            ans += -neg_val  # Add positive value to the total
            
            # If we haven't shrunk the subarray down to a single element
            if l < r:
                # Shrink from the left
                t1 = (l + 1, r)
                if t1 not in visited:
                    visited.add(t1)
                    heapq.heappush(pq, (-get_val(l + 1, r), l + 1, r))
                    
                # Shrink from the right
                t2 = (l, r - 1)
                if t2 not in visited:
                    visited.add(t2)
                    heapq.heappush(pq, (-get_val(l, r - 1), l, r - 1))
                    
        return ans
