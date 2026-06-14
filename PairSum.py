class Solution(object):
    def pairSum(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Step 3: Iterate through both halves to find the maximum twin sum
        max_sum = 0
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, twin_sum)
            
            # Move both pointers forward
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum
