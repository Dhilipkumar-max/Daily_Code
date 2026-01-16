class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7
        
        # Add boundary fences
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        # Compute all possible horizontal distances
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])
        
        # Compute all possible vertical distances
        v_dist = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_dist.add(v[j] - v[i])
        
        # Find the largest common distance
        common = h_dist & v_dist
        if not common:
            return -1
        
        side = max(common)
        return (side * side) % MOD
