# # https://leetcode.com/problems/clone-graph/

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

#         if not node:
#             return None
#         dummy = Node(node.val)
#         q = deque([(node, dummy)])

#         nodes = defaultdict(Node)
#         nodes[node] = dummy


#         while q:
#             cur, new_node = q.popleft()
#             for nxt in cur.neighbors:
#                 if nxt not in nodes:
#                     nodes[nxt] = Node(nxt.val, [new_node])
#                     q.append((nxt, nodes[nxt]))
#                     new_node.neighbors.append(nodes[nxt])
#                 elif nxt in nodes:
#                     if new_node in nxt.neighbors:
#                         continue
#                     else:
#                         nodes[nxt].neighbors.append(new_node)
#                         new_node.neighbors.append(nodes[nxt])
#         return dummy
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        dummy = Node(node.val)
        q = deque([(node, dummy)])

        nodes = {}  # ✅ defaultdict 제거
        nodes[node] = dummy

        while q:
            cur, new_node = q.popleft()
            for nxt in cur.neighbors:
                if nxt not in nodes:
                    nodes[nxt] = Node(nxt.val)  # ✅ neighbors에 new_node 넣지 말기
                    q.append((nxt, nodes[nxt]))
                new_node.neighbors.append(
                    nodes[nxt]
                )  # ✅ 있든 없든 현재 clone에만 추가

        return dummy

        # 발견한 순간 내 neighbor에만 연결하면 된다는게 헷갈렸음
