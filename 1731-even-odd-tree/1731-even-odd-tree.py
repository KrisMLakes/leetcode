# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        if not root:
            return True
        queue = deque([root])
        
        while queue:
            prev_val = None
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.popleft()

                if node:
                    if level % 2 ==0:
                        if node.val %2 ==0:
                            return False
                        if prev_val is not None and prev_val >= node.val:
                            return False

                    else:
                        if node.val %2 ==1:
                            return False
                        if prev_val is not None and prev_val <= node.val:
                            return False

                    prev_val = node.val
                    

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level +=1
        return True

        