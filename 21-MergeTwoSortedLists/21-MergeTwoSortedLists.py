# Last updated: 4/21/2026, 6:01:56 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        head = ListNode(0, None)
9        curr = head
10        while list1 and list2:
11 
12            if list1.val <= list2.val:
13                curr.next = list1
14                list1 = list1.next
15                
16            else:
17                curr.next =  list2
18                list2 = list2.next
19            curr = curr.next
20        
21        if(list1):
22            curr.next = list1
23        elif(list2):
24            curr.next = list2
25        return head.next
26                