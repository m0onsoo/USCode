# Given
#- a binary tree root
#- a binary tree subtree

# Goal
# Determine if there is a subtree of the root with the same structure

# Constraints
# root.size <= N
# no extra memory constraints

# Approach
# traverse the root binary tree recursively
# if there is a node with the same structure of subroot, examine the structure similarity recursively
# if no child nodes are structurely same, move on to the next subtree

# Example:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      
      isFound = False
      def examine(node, other) -> bool:
        if node == other:
          return examine(node.left, other.left) and examine(node.right, other.right)
        return False
        
      def traverse(node: TreeNode, other: TreeNode) -> None:
        nonlocal isFound
        # check if node is not null
        if not node or isFound:
	        return

        # check if the node is same with the other
        	# if yes, examine the structure
        if examine(node, other):
            isFound = True
        
        # move on to the left child node
        traverse(node.left, other.left)
        # if not found in the left subtree, move on to the right child node
        traverse(node.right, other.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      
        isFound = False
        def examine(node, other) -> bool:
            if not node and not other:
                return True
            if node and other and node.val == other.val:
                return examine(node.left, other.left) and examine(node.right, other.right)
            return False
        
        def traverse(node: TreeNode, other: TreeNode) -> None:
            nonlocal isFound
            # check if node is not null
            if not node or isFound:
                return

            # check if the node is same with the other
                # if yes, examine the structure
            if examine(node, other):
                isFound = True
                return
            
            # move on to the left child node
            traverse(node.left, other)
            # if not found in the left subtree, move on to the right child node
            traverse(node.right, other)

        traverse(root, subRoot)
        return isFound