# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        diff_current = 0
        diff_closest = 0
        closest = root.val
        while root:
            diff_current = abs(root.val - target)
            diff_closest = abs(closest - target)
            
            if diff_current < diff_closest or (diff_current == diff_closest and closest > root.val):
                closest = root.val
                
            if root.val > target:
                root = root.left
            elif root.val == target:
                return root.val
            elif root.val < target:
                root = root.right
                
        return closest