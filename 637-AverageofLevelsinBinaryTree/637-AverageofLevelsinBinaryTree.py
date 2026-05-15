# Last updated: 5/15/2026, 2:01:10 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
9        q = deque([root])
10
11        result = []
12
13        while q:
14            total = 0
15            level_len = len(q)
16            for i in range(level_len):
17                node = q.popleft()
18                total += node.val
19                if node.left:
20                    q.append(node.left)
21                if node.right:
22                    q.append(node.right)
23            result.append(total / level_len )
24
25        return result
26
27
28
29