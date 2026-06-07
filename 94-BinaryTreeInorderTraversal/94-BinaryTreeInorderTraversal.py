# Last updated: 6/7/2026, 5:56:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        # append to queue
10       res = []
11
12       def traverse(root):
13            if root is None:
14                return
15            
16            traverse(root.left)
17            res.append(root.val)
18            traverse(root.right)
19       traverse(root)
20       return res