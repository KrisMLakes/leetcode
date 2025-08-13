# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #    if (p.val <= (root.val) <= q.val) or (q.val <= (root.val) <= p.val):
     #       return root
      #  elif (p.val <= root.val and q.val <= root.val):
       #     return self.lowestCommonAncestor(root.left, p, q)
        #else:
         #   return self.lowestCommonAncestor(root.right, p, q)
        while root:
            # Both nodes are smaller than root → go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Both nodes are larger than root → go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # Split point found: root is between p and q → LCA
                return root
        