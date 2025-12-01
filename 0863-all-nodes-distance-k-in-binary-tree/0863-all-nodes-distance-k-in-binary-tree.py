# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def dfs(node, parent):
            if not node:
                return None
            node.parent = parent

            dfs(node.left, node)
            dfs(node.right, node)

        seen={target}
        queue = deque([target])
        dfs(root, None)
        distance = 0

        while queue and distance < k:
            curr_length = len(queue)
            for _ in range(curr_length):

                node = queue.popleft()
                for neighbor in [node.parent, node.left, node.right]:
                    if neighbor  and neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
            distance +=1
        return [node.val for node in queue]


        