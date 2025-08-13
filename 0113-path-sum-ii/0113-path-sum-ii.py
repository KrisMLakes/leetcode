# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []


        def dfs (node, current_sum, current_path):
            if not node:
                return 
            
            current_sum = current_sum + node.val
            current_path.append(node.val)

            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))
            
            dfs(node.left, current_sum, current_path)
            dfs(node.right, current_sum, current_path)

            current_path.pop()

        
        dfs(root,0,[])
        return result

        