# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                level.append(cur.val)
            ans.append(level)

        return ans

    # DFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = []
        stack.append((root, 0))

        ans = []
        while stack:
            cur, lvl = stack.pop()
            if len(ans) <= lvl:
                ans.append([cur.val])
            else:
                ans[lvl].append(cur.val)
            if cur.right:
                stack.append((cur.right, lvl + 1))
            if cur.left:
                stack.append((cur.left, lvl + 1))

        return ans

    # recursive DFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []

        def dfs(node, lvl):
            if len(ans) == lvl:
                ans.append([node.val])
            else:
                ans[lvl].append(node.val)
            if node.left:
                dfs(node.left, lvl + 1)
            if node.right:
                dfs(node.right, lvl + 1)

        dfs(root, 0)
        return ans
