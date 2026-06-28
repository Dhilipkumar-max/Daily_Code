class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: The first element must be 1
        arr[0] = 1
        
        # Step 3: Ensure the absolute difference between adjacent elements is <= 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
                
        # Step 4: The last element is the maximum possible value
        return arr[-1]
