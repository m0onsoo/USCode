# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 0ms, 17.3MB

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        stack = [root]
        while stack:
            node = stack.pop()
            
            node.left, node.right = node.right, node.left

            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        
        return root
