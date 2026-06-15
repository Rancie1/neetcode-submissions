# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
     
        queue = deque()
        queue.append(root)

        while queue:
            nodes_in_current_level = len(queue)
            current_lvl = []
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                if node:

                    current_lvl.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
            if current_lvl:
                ans.append(current_lvl)
        return ans

        