"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        node_map = dict()
        node_map[node] = Node(node.val)

        while queue:
            curr = queue.pop()
            curr_clone = node_map[curr]
            for n in curr.neighbors:
                if n not in node_map:
                    node_map[n] = Node(n.val)
                    queue.append(n)

                curr_clone.neighbors.append(node_map[n])

        return node_map[node]


