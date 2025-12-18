# https://leetcode.com/problems/merge-intervals/description/
# 56-merge-intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for s, e in intervals:
            if len(stack) > 0:
                cur_s, cur_e = stack.pop()
                if s <= cur_e:
                    stack.append((cur_s, max(cur_e, e)))
                    continue
                else:
                    stack.append((cur_s, cur_e))
            stack.append((s, e))

        return stack
