# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, cur_min, cur_max):
            if not node:
                return (cur_max - cur_min)
            cur_min = min(node.val, cur_min)
            cur_max = max(node.val, cur_max)

            right_diff = helper(node.right, cur_min, cur_max)
            left_diff = helper(node.left, cur_min, cur_max)
            return max(right_diff, left_diff)

            if not root:
                return 0
        return helper(root, root.val, root.val)
