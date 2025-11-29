class Solution(object):
    def minOperations(self, nums, k):
        S = sum(nums)
        rem = S % k
        return 0 if rem == 0 else rem
