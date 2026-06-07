# Last updated: 6/7/2026, 6:19:49 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9
10        def dfs(root):
11            if root is None:
12                return 0, True
13        
14            l = dfs(root.left)
15            r = dfs(root.right)
16            
17
18            if not l[1] or not r[1] or abs(l[0] - r[0]) > 1:
19                return 0, False
20            
21            return 1 + max(l[0], r[0]), True
22        
23        return dfs(root)[1]
24
25            
26