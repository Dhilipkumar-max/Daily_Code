# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Base cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Optimize k to avoid unnecessary full rotations
        k = k % length
        if k == 0:
            return head
            
        # Step 3: Find the new tail (which is at length - k - 1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # Step 4: Perform the rotation
        new_head = new_tail.next
        tail.next = head       # Link the old tail to the old head
        new_tail.next = None   # Break the cycle
        
        return new_head
