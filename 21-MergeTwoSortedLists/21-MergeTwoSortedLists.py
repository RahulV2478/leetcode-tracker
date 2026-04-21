# Last updated: 4/21/2026, 6:01:45 PM
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
11            print(list1.val)
12            print(list2.val)
13            if list1.val <= list2.val:
14                curr.next = list1
15                list1 = list1.next
16                
17            else:
18                curr.next =  list2
19                list2 = list2.next
20            curr = curr.next
21        
22        if(list1):
23            curr.next = list1
24        elif(list2):
25            curr.next = list2
26        return head.next
27                