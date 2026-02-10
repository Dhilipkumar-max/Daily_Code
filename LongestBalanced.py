class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            evens = set()
            odds = set()
            for j in range(i, n):
                val = nums[j]
                
                # Sort the number into the correct set
                if val % 2 == 0:
                    evens.add(val)
                else:
                    odds.add(val)
                
                # If the count of distinct numbers matches, update max_len
                if len(evens) == len(odds):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len
