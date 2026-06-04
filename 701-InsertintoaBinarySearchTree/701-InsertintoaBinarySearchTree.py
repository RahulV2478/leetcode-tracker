# Last updated: 6/3/2026, 9:57:13 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        curr = root
10        while curr:
11            if curr.val > val:
12                if curr.left:
13                    curr = curr.left
14                else:
15                    curr.left = TreeNode(val)
16                    return root
17            
18            else:
19                if curr.right:
20                    curr = curr.right
21                else:
22                    curr.right = TreeNode(val)
23                    return root
24        return TreeNode(val)
25        