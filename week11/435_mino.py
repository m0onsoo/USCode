class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        count, n, start_p, end_p = 0, len(intervals), intervals[0][0], intervals[0][1]
        # print(intervals)
        for i in range(1, n):
            curr = intervals[i]
            # print(start_p, end_p, curr)
            if (start_p <= curr[0] and curr[1] <= end_p) or curr[0] < end_p <= curr[1]:
                count += 1
            else:
                start_p = curr[0]
                end_p = curr[1]

        return count

        