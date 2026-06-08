# Last updated: 6/7/2026, 8:37:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        # mapping of values to index in the inorder list
10        # make a deque of preorder
11        # pop from the front and find its place in the inorder list
12        
13        mapping = {}
14        for idx, node in enumerate(inorder):
15            print(idx, node)
16            mapping[node] = idx
17        
18        preorder = deque(preorder)
19        def traverse(start, end):
20            if start > end:
21                return None 
22            
23            root = TreeNode(preorder.popleft())
24            mid = mapping[root.val]
25            
26            root.left = traverse(start, mid - 1)
27            root.right = traverse(mid + 1, end)
28
29            return root
30
31        
32        return traverse(0,  len(preorder) - 1)
33