# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs 혹은 bfs 둘 다 풀 수 있을듯?
        # 헷갈리니까 bfs 해보자

        queue = deque([])

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val:
            queue.append((p,q))
        else:
            return False

        while queue:
            cur_p, cur_q = queue.popleft()


            p_left, p_right = cur_p.left, cur_p.right
            q_left, q_right = cur_q.left, cur_q.right

            if p_left and not q_left:
                return False
            if not p_left and q_left:
                return False
            if p_left and q_left and p_left.val != q_left.val:
                return False
            if p_right and not q_right:
                return False
            if not p_right and q_right:
                return False
            if p_right and q_right and p_right.val != q_right.val:
                return False


            if p_left:
                queue.append((p_left, q_left))
            if p_right:
                queue.append((p_right, q_right))

        return True