# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
        diameter = 0
        def dfs(node:Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # print(left_height, right_height)
            if left_height + right_height > diameter:
                diameter = left_height + right_height

            return max(left_height, right_height) + 1
      
        dfs(root)
        return diameter