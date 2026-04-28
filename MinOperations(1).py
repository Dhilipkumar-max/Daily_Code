class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # 1. Flatten the 2D grid into a 1D list
        arr = [val for row in grid for val in row]
        
        # 2. Check if it's possible to make all elements equal
        rem = arr[0] % x
        if any(val % x != rem for val in arr):
            return -1
            
        # 3. Sort the array to find the median
        arr.sort()
        n = len(arr)
        median = arr[n // 2]
        
        # 4. Calculate the total number of operations
        return sum(abs(val - median) // x for val in arr)

