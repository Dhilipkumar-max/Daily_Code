class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.ans = 0

        def dfs(node, parent):
            total = values[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                total += dfs(nei, node)

            if total % k == 0:
                self.ans += 1
                return 0  # component formed, cut here
            return total

        dfs(0, -1)
        return self.ans
