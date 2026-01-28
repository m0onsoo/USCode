class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { i: [] for i in range(numCourses) }
        for prereq in prerequisites:
            a, b = prereq
            graph[b].append(a)

        state = [0] * numCourses
        res = []
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for adj in graph[course]:
                if not dfs(adj):
                    return False

            state[course] = 2
            res.append(course)
            return True

        for i in range(numCourses-1, -1, -1):
            if not dfs(i):
                return []
            # print(res)

        return res[::-1]