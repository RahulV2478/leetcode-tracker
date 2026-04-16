# Last updated: 4/15/2026, 11:49:48 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root, max_val):
            if root is None:
                return 0
            good_nodes = 0 
            if root.val >= max_val:
                good_nodes = 1
            
            leftNodes = dfs(root.left, max(max_val, root.val))
            rightNodes = dfs(root.right, max(max_val, root.val))
            return leftNodes + rightNodes + good_nodes
        
        return dfs(root, float('-inf'))
        