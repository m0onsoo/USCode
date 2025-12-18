class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])

        prev_end = intervals[0][1]

        cnt = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:
                cnt += 1
                prev_end = intervals[i][1] 
    
        return len(intervals) - cnt