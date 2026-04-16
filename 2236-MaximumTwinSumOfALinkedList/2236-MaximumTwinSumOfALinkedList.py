# Last updated: 4/15/2026, 11:49:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        max = 0
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while(prev):
            if(head.val + prev.val) > max:
                max = head.val + prev.val
            head = head.next
            prev = prev.next
        return max
