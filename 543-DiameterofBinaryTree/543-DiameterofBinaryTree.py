# Last updated: 6/7/2026, 6:14:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9
10        def traverse(root):
11            if root is None:
12                return 0, 0
13            
14            left, left_diameter = traverse(root.left)
15            right, right_diameter = traverse(root.right)
16
17            max_diameter = max(left + right, left_diameter, right_diameter)
18
19            return (1 + max(left, right)), max_diameter
20        
21        return traverse(root)[1]
22