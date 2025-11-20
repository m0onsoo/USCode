# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right\

# 2ms, 18.49MB
from typing import Optional, List
from tree_node import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_order = [[root.val]]
        level = []


        queue = deque([root])
        subque = deque()
        
        while queue:
            # 같은 레벨은 하나의 데크에 들어가있음. 데크 안의 노드를 순회하며 L, R 가지는지 확인
            node = queue.popleft()
            if node.left:
                level.append(node.left.val)   # 반환용 리스트
                subque.append(node.left)      # 그래프 순회용 데크
            if node.right:
                level.append(node.right.val)
                subque.append(node.right)


            if not queue:
                # 특정 레벨의 데크가 비었으면 지금까지 모아둔 레벨 리스트를 최종 리스트에 추가하고, 서브큐를 기존 데크에 덮어씌우고 다음 레벨을 위한 새로운 데크 생성
                level_order.append(level)
                level = []

                queue = subque
                subque = deque()

        return level_order[:-1]
