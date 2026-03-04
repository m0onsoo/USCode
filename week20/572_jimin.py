#  https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 처음에는 큐로 해보려고 했는데 그냥 헬퍼펑션으로 뺴는게 훨씬 간단했음 
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        def isSame(node1, node2):
            if node1 == node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)

        
        while q:
            cur = q.popleft()
            if cur.val == subRoot.val:
                same = isSame(cur, subRoot)
                if same:
                    return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return False
