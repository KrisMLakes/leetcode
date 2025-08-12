# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        root1 = root
        if not root:
            return None
        while queue:

                node = queue.popleft()

                node.right, node.left = node.left, node.right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root1




        