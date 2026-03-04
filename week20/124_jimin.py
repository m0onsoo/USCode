# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/1938130444/?q=155
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.opt_path = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            # print(left, right, node.val)

            max_path = max(left + node.val, right + node.val)
            self.opt_path = max(self.opt_path, left + right + node.val, max_path, node.val)

            return max(max_path, node.val) # 리턴할때는 한쪽으로 내려간거 혹은 자기 자신만.

        dfs(root)
        return self.opt_path