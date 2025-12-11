# https://leetcode.com/problems/course-schedule/
# 207-course-schedule

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = defaultdict(int)
        # calculate indegree
        for a, b in prerequisites:
            indegree[b] += 1

        # create hashmap for relations
        need_class = defaultdict(list)
        for a, b in prerequisites:
            need_class[a].append(b)

        q = deque([])
        # count indegree == 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        remaining = numCourses
        while q:
            cur = q.popleft()
            for c in need_class[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            remaining -= 1

        return True if remaining == 0 else False

        # while indegree_zero > 1:
        #     for course in courses:
        #         if indegree[course] == 0:
        #             for c in need_class[course]:
        #                 indegree[c] -= 1
        #                 if indegree[c] == 0:
        #                     indegree_zero += 1
        #             indegree_zero -= 1
        #             del indegree[course]

        # if len(indegree) > 0:
        #     return False
        # else: return True
