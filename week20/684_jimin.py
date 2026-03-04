# https://leetcode.com/problems/redundant-connection/?q=155

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
        parent = [i for i in range(len(edges) + 1)]
        rank = [0 for _ in range(len(edges) + 1)]

        def find(a):    
            if parent[a] == a:
                return a
            else:
                p = find(parent[a])
            return p

        def union(a, b):
            p_a, p_b = find(a), find(b)

            if p_a == p_b:
                return False
            if rank[p_a] == rank[p_b]:
                parent[p_b] = p_a
                rank[p_a] += 1
            elif rank[p_a] > rank[p_b]:
                parent[p_b] = p_a
            elif rank[p_a] < rank[p_b]:
                parent[p_a] = p_b
            return True

        for a, b in edges:
            res = union(a,b)
            if not res:
                return [a,b]
