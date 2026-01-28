# https://leetcode.com/problems/course-schedule-ii/
# 210
# Topological Ordering

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        indegree = [0] * numCourses # 아직 못채운 조건의 개수
        for a, b in prerequisites:
            graph[b].append(a) # b를 들어야 a를 들을 수 있음
            indegree[a] += 1

        q = deque()

        for i, degree in enumerate(indegree):
            if degree == 0:
                q.append(i)

        ans = []
        while q:
            cur = q.popleft()
            for course in graph[cur]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
            ans.append(cur)

        return ans if len(ans) == numCourses else []
        