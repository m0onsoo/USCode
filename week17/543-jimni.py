# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs 하면서 내려가면서 왼쪽 오른쪽각각 max 해서 더하면?
        self.ans = 0

        def dfs(node):

            left, right  = 0, 0
            if node.left:
                left = dfs(node.left) + 1
            if node.right:
                right = dfs(node.right) + 1


            max_depth = max(left, right)

            self.ans = max(self.ans, left + right)
            return max_depth

        dfs(root)

        return self.ans
            