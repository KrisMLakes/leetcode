# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = []

        def dfs (node, path_sums):
            if not node:
                return 0
            
            count = 0

            path_sums = [node.val + x for x in path_sums] + [node.val]
            count += path_sums.count(targetSum)
            
            count += dfs(node.left, path_sums)
            count += dfs(node.right, path_sums)
            return count

        return dfs(root,[])
 

        