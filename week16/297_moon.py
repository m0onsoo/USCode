# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# 82ms, 22.46MB
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            # edge case
            return ""
        
        # 각 노드의 val 사이를 . 구분자로 구분 (음수 혹은 여러 자리 수의 숫자 케이스를 고려하기 위함)
        data = str(root.val)
        data += "."
        
        # BFS로 순회하면서 string에 추가
        queue = deque([root])
        while queue:
            node = queue.popleft()
            l, r = node.left, node.right
            data += "N" if l is None else str(l.val)
            data += "."
            data += "N" if r is None else str(r.val)
            data += "."

            if l is not None:
                queue.append(l)
            if r is not None:
                queue.append(r)

        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is "":
            # edge case
            return None

        i = 0
        # 구분자에 도달할 때까지 인덱스 증가
        while data[i] != '.':
            i += 1
        root = TreeNode(val = data[:i])
        queue = deque([root])
        
        i += 1   # i가 구분자를 가리키고 있기에 한칸 더 가서 . 구분자를 넘겨줘야 함
        # 마찬가지로 BFS 순서로 순회하면서 노드 생성하고 트리에 추가
        while(queue):
            # 구분자까지의 인덱스 계산
            idx_l = i
            while data[i] != '.':
                i += 1
            l = None if data[idx_l:i] == 'N' else TreeNode(val = data[idx_l:i])
            i += 1

            idx_r = i
            while data[i] != '.':
                i += 1
            r = None if data[idx_r:i] == 'N' else TreeNode(val = data[idx_r:i])
            i += 1
        
            node = queue.popleft()
            node.left, node.right = l, r

            if l is not None:
                queue.append(l)
            if r is not None:
                queue.append(r)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))