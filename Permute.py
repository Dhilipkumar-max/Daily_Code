class Solution(object):
    def permute(self, nums):
        result = []
        
        def backtrack(current_permutation, visited):
            # Base case: if the current path has the same length as nums,
            # we found a valid permutation.
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            # Explore choices
            for num in nums:
                if num not in visited:
                    # 1. Make a choice
                    visited.add(num)
                    current_permutation.append(num)
                    
                    # 2. Recurse to build the rest of the permutation
                    backtrack(current_permutation, visited)
                    
                    # 3. Backtrack (undo the choice)
                    current_permutation.pop()
                    visited.remove(num)
                    
        backtrack([], set())
        return result
