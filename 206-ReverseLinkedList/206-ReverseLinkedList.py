# Last updated: 4/21/2026, 5:32:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9
10        prev = None
11        while head:
12            temp = head.next
13            head.next = prev
14            prev = head
15            head = temp
16
17        return prev
18