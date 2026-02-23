# https://leetcode.com/problems/balanced-binary-tree/submissions/1928218547/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs로 내려가면서 리턴한 레프트 라이트가 하나 차이나면 괜춘
        # 제일 큰걸 리턴


        self.ans = True
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1

            if abs(left - right) > 1:
                self.ans = False
            return max(left, right)

        dfs(root)
        return self.ans