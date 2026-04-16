# Last updated: 4/15/2026, 11:49:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse the linked list
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        max_val = prev.val  # Initialize max with the first node's value
        temp = prev  # Keep track of the head of the reversed list
        current = prev
        
        while current and current.next:
            if current.next.val >= max_val:
                max_val = current.next.val  
                current = current.next  
            else:
                current.next = current.next.next
        prev = None
        while temp:
            curr = temp
            temp = temp.next
            curr.next = prev
            prev = curr
        return prev