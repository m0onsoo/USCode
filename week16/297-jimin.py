# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = ''

        q = deque()

        if root:
            q.append(root)
            string += str(root.val)


        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    string += ',' + str(cur.left.val)
                    q.append(cur.left)
                else:
                    string += ',' + 'null'
                if cur.right:
                    string += ',' + str(cur.right.val)
                    q.append(cur.right)
                else:
                    string += ',' + 'null'
        print(string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None
        
        values = data.split(',')
        print(values)
        nodes = {}
        for i, val in enumerate(values):
            if val == 'null':
                continue
            node = TreeNode(val)
            nodes[i] = node

        for i, val in enumerate(values):
            if val == 'null':
                continue
            
            nodes[i].left = nodes[i * 2 + 1]
            nodes[i].right = nodes[i * 2 + 2]

        return nodes[0]

    def deserialize(self, data):
        if not data:
            return None
            
        values = data.split(',')
        root = TreeNode(int(values[0]))
        
        q = deque([root])
        
        i = 1 
        
        # 큐에 부모가 있고, 아직 읽을 데이터가 남은 동안 반복
        while q and i < len(values):
            parent = q.popleft()
            
            # 1. 왼쪽 자식 연결
            if values[i] != 'null':
                node = TreeNode(int(values[i]))
                parent.left = node
                q.append(node)
            i += 1 # null이든 아니든 인덱스는 전진해야 함
            
            # 2. 오른쪽 자식 연결 (범위 체크 필수)
            if i < len(values) and values[i] != 'null':
                node = TreeNode(int(values[i]))
                parent.right = node
                q.append(node)
            i += 1
            
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))