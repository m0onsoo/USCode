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

        visited = {}
        visited[node] = Node(node.val)
        
        stack = [node]
        while stack:
            curr_node = stack.pop()
            for n in curr_node.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    stack.append(n)

                visited[curr_node].neighbors.append(visited[n])
        
        return visited[node]