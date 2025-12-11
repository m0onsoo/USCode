from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_deg = defaultdict(int) 
        deg2c = defaultdict(list)   # key: in-degree, values: list of courses
        pre2subs = defaultdict(list)  # key: pre, values: list of subsequent courses

        for i in range(numCourses):
            in_deg[i] = 0
        for sub, pre in prerequisites:
            in_deg[sub] += 1
            pre2subs[pre].append(sub)
        
        for key, val in in_deg.items():
            deg2c[val].append(key)
        
        # print(in_deg)
        # print(deg2c)
        
        topological_order = ""
        cnt = 0
        
        if not deg2c[0]:
            return False
        while len(deg2c[0]) > 0:
            pre_c = deg2c[0].pop()
            cnt += 1

            for sub in pre2subs[pre_c]:
                degree = in_deg[sub]
                deg2c[degree].remove(sub) # degree: sub courses에서 제거

                in_deg[sub] -= 1
                deg2c[degree - 1].append(sub) # 새로운 degree에 넣어줌

        return cnt == numCourses