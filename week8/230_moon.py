# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 0ms, 21.18MB
from typing import Optional
from tree_node import TreeNode
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        deq = deque([root])
        while deq:
            # 그래프를 순회하면서 모든 밸류를 리스트에 추가
            node = deq.popleft()
            nums.append(node.val)

            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)
        # 리스트 정렬 후 k번째 원소 반환
        nums.sort()
        return nums[k-1]