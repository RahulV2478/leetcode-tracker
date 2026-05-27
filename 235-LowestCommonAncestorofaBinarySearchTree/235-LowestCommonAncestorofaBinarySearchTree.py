# Last updated: 5/27/2026, 1:22:42 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        
11        while root:
12            if root.val <= p.val and root.val >= q.val:
13                return root
14            if root.val <= q.val and root.val >= p.val:
15                return root
16            if root.val < q.val and root.val < p.val:
17                root = root.right
18            if root.val > q.val and root.val > p.val:
19                root = root.left
20
21