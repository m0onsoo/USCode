# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Kth smallest == heap?? no
# DFS로 왼쪽으로 쭉 내려갔다가 올라오면서 count 하면 되지 않을까
# Inorder Traversal


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0

        def dfs(node):
            if node.left:
                val = dfs(node.left)
                if val is not None:
                    return val
            self.count += 1
            if self.count == k:
                return node.val
            if node.right:
                val = dfs(node.right)
                if val is not None:
                    return val

        return dfs(root)

        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            stack = []
            cur = root
            count = 0

            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                count += 1

                if count == k:
                    return cur.val

                cur = cur.right
