# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(node) -> List[int]:
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        arr1 = inorder(root1)
        arr2 = inorder(root2)

        merged = []
        i,j = 0,0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i +=1
            else:
                merged.append(arr2[j])
                j +=1
            
        merged += arr1[i:]
        merged += arr2[j:]

        return merged




        