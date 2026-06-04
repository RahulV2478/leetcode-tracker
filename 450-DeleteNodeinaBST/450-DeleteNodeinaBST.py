# Last updated: 6/3/2026, 10:21:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9        
10        if root is None:
11            return None
12        
13        if root.val < key:
14            root.right = self.deleteNode(root.right, key)
15        
16        elif root.val > key:
17            root.left = self.deleteNode(root.left, key)
18        
19        else:
20
21            if not root.left and not root.right:
22                return None
23            if not root.left:
24                return root.right
25            if not root.right:
26                return root.left
27            
28            successor = root.left
29
30            while successor.right:
31                successor = successor.right
32            
33            root.val = successor.val
34            root.left = self.deleteNode(root.left, successor.val)
35            
36            return root
37
38        return root
39
40        
41        