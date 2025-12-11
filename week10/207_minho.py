class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = [course]
            else:
                graph[prereq].append(course)

        visited = set()      
        rec_stack = set()   

        def dfs(course):
            # If re-encountered in current path → cycle
            if course in rec_stack:
                return False
            
            # Already checked and safe
            if course in visited:
                return True

            # Mark as visiting
            rec_stack.add(course)

            # Explore neighbors if any
            if course in graph:
                for next_course in graph[course]:
                    if not dfs(next_course):
                        return False

            # Done exploring, move from rec_stack to visited
            rec_stack.remove(course)
            visited.add(course)
            return True

        # Run DFS from all courses
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
