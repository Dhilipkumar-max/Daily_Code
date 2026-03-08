class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res = []
        for i in range(len(nums)):
            # Look at the i-th character of the i-th string
            curr = nums[i][i]
            
            # Flip it: if '0' make it '1', if '1' make it '0'
            res.append('1' if curr == '0' else '0')
            
        return "".join(res)
