# Last updated: 5/27/2026, 1:19:25 AM
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
11        
12        
13        def search(root, p, q):
14            if root is None:
15                return None
16            
17            if root.val <= p.val and root.val >= q.val:
18                return root
19            
20            elif root.val <= q.val and root.val >= p.val:
21                return root
22            
23            
24            left = search(root.left, p, q)
25            right = search(root.right, p, q)
26            return left or right
27        
28        return search(root, p, q)
29