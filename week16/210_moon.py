from collections import defaultdict, deque

# 0ms, 20.32MB
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a, b] == b -> a

        order = []

        # DAG
        pre2post = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in prerequisites:
            # key: 선수과목, value: 후수과목
            pre2post[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                # in-degree가 초기에 0인 노드들 추가
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for post in pre2post[course]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    queue.append(post)

        if len(order) == numCourses:
            return order
        else:
            return []