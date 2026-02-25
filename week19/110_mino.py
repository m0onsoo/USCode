# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def countDepth(root:Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            l_depth = countDepth(root.left)
            r_depth = countDepth(root.right)

            if abs(l_depth - r_depth) > 1:
                self.res = False
            return max(l_depth, r_depth) + 1

        cnt = countDepth(root)
        return self.res