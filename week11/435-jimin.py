# https://leetcode.com/problems/non-overlapping-intervals/description/
# 435-non-overlapping-intervals


class Solution:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # sort by 1, 2

    # intervals.sort(key=lambda x: (x[0], x[1]))

    # stack = [intervals[0]]

    # print(intervals)

    # ans = 0
    # for s, e in intervals[1:]:
    #     cur_s, cur_e = stack.pop()

    #     if s < cur_e:
    #         stack.append([cur_s, cur_e])
    #         ans += 1
    #         continue
    #     else:
    #         stack.append([cur_s, cur_e])
    #         stack.append([s,e])
    # return ans

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        stack = [intervals[0]]
        ans = 0
        for s, e in intervals[1:]:
            cur_s, cur_e = stack.pop()
            if s < cur_e:
                stack.append([cur_s, cur_e])
                ans += 1
                continue
            else:
                stack.append([cur_s, cur_e])
                stack.append([s, e])
        return ans
