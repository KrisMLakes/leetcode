# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        level = 0
        ans = []
        while queue:
            i = 0
            num_of_nodes = len(queue)
            level_nodes = []
            for _ in range(num_of_nodes):
                
                #if level%2 == 0:
                node = queue.popleft()
                    #print(node.val)
               
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level %2 == 1:
                level_nodes.reverse()
                
            ans.append(level_nodes)
            level +=1
            
        return ans
            
        