class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            # Find the first 0 from the right in the binary representation
            # We want to flip the 1 that is immediately to the right of that 0
            # to minimize the reduction from p.
            
            for i in range(31):
                # Check if the i-th bit is 0
                if not (p & (1 << i)):
                    # The bit to flip is the (i-1)-th bit
                    # This bit must exist because p is an odd prime (> 2)
                    res = p ^ (1 << (i - 1))
                    ans.append(res)
                    break
        return ans
