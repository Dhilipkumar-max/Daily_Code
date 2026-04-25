class Solution(object):
    def maxDistance(self, side, points, k):
        p = []
        # Map 2D boundary points to 1D perimeter coordinates
        for x, y in points:
            if y == 0:
                p.append(x)
            elif x == side:
                p.append(side + y)
            elif y == side:
                p.append(2 * side + (side - x))
            elif x == 0:
                p.append(3 * side + (side - y))
                
        p.sort()
        n = len(p)
        
        # Array `A` replicates the perimeter to simulate wrap-around easily
        A = [0] * (2 * n)
        for i in range(n):
            A[i] = p[i]
            A[i + n] = p[i] + 4 * side
            
        def check(D):
            # Precompute jumps: nxt[i] will store the smallest index j such that A[j] - A[i] >= D
            nxt = [2 * n] * (2 * n + 1)
            j = 0
            for i in range(2 * n):
                while j < 2 * n and A[j] - A[i] < D:
                    j += 1
                nxt[i] = j
                
            # Attempt placing `k` points starting from each point `i`
            for i in range(n):
                curr = i
                target = i + n
                for _ in range(k):
                    curr = nxt[curr]
                    if curr > target:  # Fails to accommodate k intervals of length D locally
                        break
                if curr <= target:     # Successfully wrapped within the bounds
                    return True
            return False
            
        # Binary search for the maximum possible minimum distance
        low = 1
        high = (4 * side) // k 
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid       # It's possible to maintain distance `mid`, seek a larger one
                low = mid + 1
            else:
                high = mid - 1  # `mid` distance breaks, seek a smaller one
                
        return ans

