import collections

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        dsu = DSU(n)
        
        # 1. Union all allowed swaps to form connected components of indices
        for u, v in allowedSwaps:
            dsu.union(u, v)
            
        # 2. Group indices by their component root
        components = collections.defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            components[root].append(i)
            
        hamming_distance = 0
        
        # 3. For each component, compare available source elements to target requirements
        for indices in components.values():
            # Count available numbers from the source in this component
            source_counts = collections.Counter(source[i] for i in indices)
            
            for i in indices:
                target_val = target[i]
                if source_counts[target_val] > 0:
                    # We can match this element
                    source_counts[target_val] -= 1
                else:
                    # Mismatch found
                    hamming_distance += 1
                    
        return hamming_distance
