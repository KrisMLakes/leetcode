# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        def getList(node) -> List[int]:
            queue = deque([node])
            ans = []
            while queue:
                num_nodes = len(queue)
                for _ in range(num_nodes):
                    node = queue.popleft()
                    if node:
                        ans.append(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
            return ans
        
        arr1 = getList(root1)
        arr2 = getList(root2)
        print(arr1, arr2)
        combined = arr1 + arr2
        combined.sort()
        return combined


        