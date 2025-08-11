# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node) -> int:
            if not node:
                return 0
            return max(maxDepth(node.left), maxDepth(node.right)) + 1
        
        queue = deque([root])
        level_count, deepestSum = 0, 0
        maxDepth_ = maxDepth(root)
        
        
        while queue:
            number_of_nodes = len(queue)
            level_count+=1 
            for _ in range(number_of_nodes):
                node = queue.popleft()
                if level_count == maxDepth_:
                    deepestSum+= node.val
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return deepestSum
        
        
        
        
        