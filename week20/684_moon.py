from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # undirected G, no cycle
        # n nodes labed from 1 to n

        # can we assume the graph is not empty? And what should I return if the graph has only one node?
        # A: not empty, n >= 3

        # Solution:
        # if we meet an edge that makes cycle, we need to update such edge
        # iterate each edge, check if a and b have shared node using set DS which takes O(1) to compare two set, if yes update added edge
        # O(n) time complexity

        # Test 1:
        # edge = [1, 2]. no intersection. graph = {1: [2], 2: [1]}
        # edge = [1, 3]. no intersection. graph = {1: [2, 3], 2: [1], 3:[1]}
        # edge = [2, 3]. graph = {1: [2, 3], 2: [1], 3:[1]}. added_edge = [2, 3]

        # Test 2:
        # edge = [1, 2]. no intersection. graph = {1: [2], 2: [1]}
        # edge = [2, 3]. no intersection. graph = {1: [2], 2: [1, 3], 3: [2]}
        # edge = [3, 4]. no intersection. graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        # edge = [1, 4]. no intersection. graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}

        def DFS(a: int, b: int) -> bool:
            visited = set()

            stack = [a]
            visited.add(a)
            while stack:
                node = stack.pop()
                if node == b:
                    return True
                    
                for adj in graph[node]:
                    if adj not in visited:
                        stack.append(adj)
                        visited.add(adj)
            return False

        def BFS(a: int, b: int) -> bool:
            visited = set()

            queue = deque([a])
            visited.add(a)
            while queue:
                node = queue.popleft()
                if node == b:
                    return True
                    
                for adj in graph[node]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            return False
        
        graph = defaultdict(set)
        added_edge = []
        for a, b in edges:
            # a < b
            if BFS(a, b):
                # if there is a path from a to b
                added_edge = [a, b]
            
            # construct a graph
            graph[a].add(b)
            graph[b].add(a)
        
        return added_edge