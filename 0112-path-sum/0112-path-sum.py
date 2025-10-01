# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, pathSum):
            if not node:
                return False
            if node.left == None and node.right == None:
                return (pathSum + node.val) == targetSum
            pathSum += node.val
            left = dfs(node.left, pathSum)
            right = dfs(node.right, pathSum)
            return left or right
        return dfs(root, 0)
        