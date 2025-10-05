# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, ans):
            if not node:
                return 0
            ans +=1
            
            
            #dfs(node.right, ans)
            return dfs(node.left, ans) + dfs(node.right, ans) + 1
        return dfs(root, ans)
            
        