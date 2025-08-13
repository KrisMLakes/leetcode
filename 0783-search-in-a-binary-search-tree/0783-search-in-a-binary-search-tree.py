# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return null
        queue = deque([root])
        #qu
        ans = []
        while queue:
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.popleft()
                if node.val == val:
                    return node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None



