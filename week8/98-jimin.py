# https://leetcode.com/problems/validate-binary-search-tree/description/
# 98-validate-binary-search-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            for _ in range(len(q)):  # don't need..
                cur, floor, ceil = q.popleft()
                if cur.left:
                    if not floor < cur.left.val < cur.val:
                        return False
                    else:
                        q.append((cur.left, floor, cur.val))

                if cur.right:
                    if not cur.val < cur.right.val < ceil:
                        return False
                    else:
                        q.append((cur.right, cur.val, ceil))
        return True

    # DFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        stack.append((root, float("-inf"), float("inf")))
        while stack:
            cur, floor, ceil = stack.pop()
            if cur.right:
                if not cur.val < cur.right.val < ceil:
                    return False
                stack.append((cur.right, cur.val, ceil))
            if cur.left:
                if not floor < cur.left.val < cur.val:
                    return False
                stack.append((cur.left, floor, cur.val))

        return True

    # Recursive DFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, floor, ceil):
            if not floor < node.val < ceil:
                return False
            left, right = True, True
            if node.left:
                left = dfs(node.left, floor, node.val)
            if node.right:
                right = dfs(node.right, node.val, ceil)
            return left and right

        return dfs(root, float("-inf"), float("inf"))
