class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # DSU structures
        parent = list(range(n))
        max_val = nums[:]  # Stores the maximum value reachable for the component
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                # Merge the components and update the root with the maximum value found
                max_val[root_j] = max(max_val[root_i], max_val[root_j])
            return root_j

        stack = []
        
        # Traverse and union connected components 
        for i in range(n):
            curr_root = i
            
            # While the stack has components and the top component's max value 
            # is strictly greater than the current element, they are connected.
            while stack and max_val[stack[-1]] > nums[i]:
                top_root = stack.pop()
                curr_root = union(curr_root, top_root)
                
            stack.append(curr_root)
            
        # Assign the final max value of its connected component to each index
        ans = [0] * n
        for i in range(n):
            ans[i] = max_val[find(i)]
            
        return ans
