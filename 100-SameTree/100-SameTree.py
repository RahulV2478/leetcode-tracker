# Last updated: 5/27/2026, 12:11:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        
10        
11        def dfs(p, q):
12            if not p and not q:
13                return True
14            if not p or not q or p.val != q.val:
15                return False
16            
17            return dfs(p.left, q.left) and dfs(p.right, q.right)
18            
19        return dfs(p, q)
20            
21
22                