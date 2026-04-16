# Last updated: 4/15/2026, 11:49:49 PM
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node):
            if not node:
                return None
            
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            
            if not node.left and not node.right and node.val == target:
                return None
            
            return node
        
        return traverse(root)
