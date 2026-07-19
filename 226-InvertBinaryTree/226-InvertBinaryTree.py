# Last updated: 7/19/2026, 12:37:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if root is None:
10            return None
11
12        root.left, root.right = root.right, root.left
13
14        root.left = self.invertTree(root.left)
15        root.right = self.invertTree(root.right)
16
17        return root
18        