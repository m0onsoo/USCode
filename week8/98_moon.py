# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List
from tree_node import TreeNode

# 1ms, 20.18MB     
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 중위 순회 후 정렬되어 있는지 여부를 리턴
        result = self.inorder_traverse(root, [])
        return result == sorted(set(result))
        
    def inorder_traverse(self, node: TreeNode, result: List):
        if node == None:
            return
        self.inorder_traverse(node.left, result)
        result.append(node.val)
        self.inorder_traverse(node.right, result)

        return result



