# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            # root = [] 인 케이스 존재
            return 0
        
        res = 0

        stack = []
        stack.append((root, 1))

        # DFS
        while stack:
            node, cur_depth = stack.pop()
            # 최대 깊이 갱신
            res = max(res, cur_depth)

            # 자식 노드가 존재할 경우, 현재 깊이 +1 과 함께 스택에 추가
            if node.left:
                stack.append((node.left, cur_depth + 1))
            if node.right:
                stack.append((node.right, cur_depth + 1))
        
        return res