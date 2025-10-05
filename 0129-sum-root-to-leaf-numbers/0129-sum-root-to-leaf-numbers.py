# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cursum):
            if not node:
                return 0
            cursum = cursum*10 + node.val
            if node.left is None and node.right is None:
                return cursum
            return dfs(node.left, cursum) + dfs(node.right, cursum)
            

        return dfs(root, 0)
        