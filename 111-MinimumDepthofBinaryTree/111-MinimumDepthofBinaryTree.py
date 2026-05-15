# Last updated: 5/15/2026, 2:13:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: Optional[TreeNode]) -> int:
9        q = deque([root])
10        level = 1
11        if not root:
12            return 0
13        while q:
14            level_size = len(q)
15            for i in range(level_size):
16                
17                node = q.popleft()
18                
19                if not node.left and not node.right:
20                    return level
21                if node.left:
22                    q.append(node.left)
23                if node.right:
24                    q.append(node.right)
25            level += 1
26
27        return