# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isPalindrome(arr:List) -> bool:
            length = len(arr)
            first, last = 0,length-1
            for _ in range(int(length/2)):
                if arr[first] != arr[last]:
                    return False
                first +=1
                last -=1
            return True

        if not root:
            return True
        queue = deque([root])
        while queue:
            level_vals = []
            num_of_nodes = len(queue)
            for _ in range(num_of_nodes):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)
            if not isPalindrome(level_vals):
                return False
            
        return True
                
            


        