# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        if not root:
            return 0
        level_count = 0
        
        max_level = 1
        max_sum = float("-inf")
        while queue:
            num_nodes = len(queue)
            level_sum = 0

            for _ in range(num_nodes):
                node = queue.popleft()
                if node:
                    level_sum +=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level_count += 1
            if max_sum < level_sum:
                max_level = level_count
            max_sum = max(max_sum, level_sum)

        return max_level

        