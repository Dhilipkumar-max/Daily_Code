class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        # Initialize the distance matrix with infinity
        # There are 26 lowercase English letters
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        # Distance from a character to itself is 0
        for i in range(26):
            dist[i][i] = 0
            
        # Fill the initial costs from the input arrays
        for o, c, z in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            # There might be multiple paths between same chars; keep the minimum
            dist[u][v] = min(dist[u][v], z)
            
        # Floyd-Warshall Algorithm: Find shortest paths between all pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            
            u = ord(s_char) - ord('a')
            v = ord(t_char) - ord('a')
            c = dist[u][v]
            
            if c == inf:
                return -1
            total_cost += c
            
        return total_cost
