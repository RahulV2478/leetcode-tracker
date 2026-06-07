# Last updated: 6/7/2026, 6:12:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        max_diameter = [0]
10
11        def traverse(root):
12            if root is None:
13                return 0
14            
15            left = traverse(root.left)
16            right = traverse(root.right)
17
18            max_diameter[0] = max(left + right, max_diameter[0])
19
20            return 1 + max(left, right)
21        
22        traverse(root)
23
24        return max_diameter[0]