# Last updated: 11/10/2026, 4:59:10 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6# Definition for a binary tree node.
7# class TreeNode:
8#     def __init__(self, val=0, left=None, right=None):
9#         self.val = val
10#         self.left = left
11#         self.right = right
12class Solution:
13    def isSubPath(self, head, root):
14        def match(root, node):
15            if not node:
16                return True
17            if not root:
18                return False
19            if root.val != node.val:
20                return False
21
22            return match(root.left, node.next) or match(root.right, node.next)
23
24        if not head:
25            return True
26
27        if not root:
28            return False
29
30        return (
31            match(root, head)
32            or self.isSubPath(head, root.left)
33            or self.isSubPath(head, root.right)
34        )