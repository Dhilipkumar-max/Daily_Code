class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
      Optional[ListNode]
        remove_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr:
            if curr.val in remove_set:
                prev.next = curr.next  # Skip the current node
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
