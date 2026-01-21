# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# 104-maximum-depth-of-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        if root == None:
            return 0

        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return level


# 만약 root가 None이라면, 코드의 첫 줄이 실행될 때 q는 다음과 같이 생성됩니다.

# Python
# q = deque([None])
# 이때 큐는 비어있는 상태가 아닙니다. None이라는 원소를 하나 가지고 있는 상태가 됩니다.
