class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        cs, ce, n = -1, -1, len(intervals)
        intervals.sort(key=lambda x:x[0])
        
        while i < n:
            prev = intervals[i]
            while i < n and prev[1] >= intervals[i][0]""
        for i in range(n+1):
            if i == n:
                res.append([cs, ce])
                break
            s, e = intervals[i][0], intervals[i][1]
            if s <= ce:
                ce = max(ce, e)
            else:
                res.append([cs, ce])
                cs = s
                ce = e

        # print(res)
        return res[1:]
        