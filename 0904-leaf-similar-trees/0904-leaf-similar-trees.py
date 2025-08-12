# Definition for a binary tree node.
class Solution:    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def findLeaves(root) -> List:
            ans = []
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]

            return findLeaves(root.right) + findLeaves(root.left)
        
        return findLeaves(root1) == findLeaves(root2)

        