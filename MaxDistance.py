class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        max_dist = 0
        
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            # Check the condition: nums1[i] <= nums2[j]
            # Note: the condition i <= j is naturally handled because 
            # if i > j, j - i will be negative and won't update max_dist.
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # nums1[i] is too big, move to a smaller number in nums1
                i += 1
                
        return max_dist
