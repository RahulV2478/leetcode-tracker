# Last updated: 5/27/2026, 2:04:24 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        if not root:
10            return TreeNode(val)
11        curr = root
12        while curr:
13            if curr.val < val:
14                if not curr.right:
15                    curr.right = TreeNode(val)
16                    return root
17                curr = curr.right
18                      
19            if curr.val > val:
20                if not curr.left:
21                    curr.left = TreeNode(val)
22                    return root
23                curr = curr.left
24            
25        return root
26            
27
28       
29            