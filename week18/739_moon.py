# 74ms, 28.92MB
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        answer = [0] * len(temperatures)

        stack = [] # element: day
        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prior_day = stack.pop()
                answer[prior_day] = day - prior_day
            
            stack.append(day)
        
        return answer