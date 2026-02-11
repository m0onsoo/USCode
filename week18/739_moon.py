# 103ms, 35.23MB
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, prev_t = stack.pop()
                answer[prev_i] = idx - prev_i
            
            stack.append((idx, temp))
        
        return answer