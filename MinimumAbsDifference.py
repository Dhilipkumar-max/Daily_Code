class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # Step 1: Sort the array in ascending order
        arr.sort()
        
        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        
        # Step 3: Find all pairs with that min_diff
        result = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result
