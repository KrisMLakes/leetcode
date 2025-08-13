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

            
        def returnBST(node) -> List:
            if not node:
                return null
            queue1 = deque([node])
            ans = []
            while queue1:
                num_nodes2 = len(queue1)
                for _ in range(num_nodes2):
                    node2 = queue.popleft()
                    ans.append(node2.val)
                    if node2.left:
                        queue1.append(node2.left)
                    if node2.right:
                        queue1.append(node2.right)
            return ans



