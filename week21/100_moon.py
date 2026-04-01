# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            # Both p and q are Null
            return True
        elif p is None or q is None:
            # Either p or q is Null
            return False

        p_queue = deque([(p, 1)])
        q_queue = deque([(q, 1)])

        while p_queue and q_queue:
            p_node, p_idx = p_queue.popleft()
            q_node, q_idx = q_queue.popleft()

            if p_node.val == q_node.val and p_idx == q_idx:
                if p_node.left:
                    p_queue.append((p_node.left, p_idx * 2))
                if p_node.right:
                    p_queue.append((p_node.right, p_idx * 2 + 1))

                if q_node.left:
                    q_queue.append((q_node.left, q_idx * 2))
                if q_node.right:
                    q_queue.append((q_node.right, q_idx * 2 + 1))
            else:
                return False
        
        print(p_queue, q_queue)
        # Return True if both p_queue and q_queue are empty, else if there is remaining, return False
        return True if not(p_queue or q_queue) else False