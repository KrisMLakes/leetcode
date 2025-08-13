# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            num_nodes = len(queue)
            avg = 0
            level_sum = 0
            
            for _ in range(num_nodes):
                node = queue.popleft()
                if node:
                    level_sum += node.val
                    #count +=1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            #avg = 
            ans.append(level_sum / num_nodes)
        return ans

            

        