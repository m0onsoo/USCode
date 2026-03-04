# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.cur_max = root.val
        # left, right, left + right
        # cur_max = max(left, right , left+right) + node.val
        # top -> max(left, right) + node.val

        def DFS(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0

            l_max = max(0, DFS(node.left))
            r_max = max(0, DFS(node.right))
            
            self.cur_max = max(self.cur_max, l_max + r_max + node.val)
            
            return max(l_max, r_max) + node.val
        
        DFS(root)
        return self.cur_max