# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.result = True

        def DFS(node: Optional[TreeNode], depth: int) -> int:
            # Calculate the depth of the tree
            if node is None:
                return depth
            
            # left_depth, right_depth = 0, 0
            # 1. l = r = depth / 2. give l_depth + 1     
            left_depth = right_depth = depth
            if node.left:
                left_depth = DFS(node.left, depth + 1)
            if node.right:
                right_depth = DFS(node.right, depth + 1)    

            # check if the tree is height-balanced
            self.result = self.result and abs(left_depth - right_depth) <= 1

            depth = max(depth, left_depth, right_depth)
            return depth

        DFS(root, 0)
        return self.result