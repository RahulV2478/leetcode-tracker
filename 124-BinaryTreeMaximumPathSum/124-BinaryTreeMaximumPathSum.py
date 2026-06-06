# Last updated: 6/5/2026, 9:05:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        max_val = [-float('inf')]
10
11        def traverse(root, max_val):
12            if root is None:
13                return 0
14
15
16            left = max(traverse(root.left, max_val), 0)
17            right = max(traverse(root.right, max_val), 0)
18
19            top = left + right + root.val
20
21            max_val[0] = max(top, max_val[0])
22            print(max_val)
23            continued = max(left, right) + root.val
24
25            return continued
26        traverse(root, max_val)
27        return max_val[0]
28
29