class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        
        result = []
        result.append(intervals[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for start, end in intervals[1:]:
            if start <= prev_end:
                # overlapping이면 interval을 이어줌
                result.pop()
                result.append([prev_start, max(end, prev_end)])

            else:
                # 겹치지 않으면 그대로 추가
                result.append([start, end])
            
            prev_start, prev_end = result[-1][0], result[-1][1]


        return result