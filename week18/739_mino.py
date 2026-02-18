class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        for i, temp in enumerate(temperatures):
            cnt = 1
            for j in range(i+1, n):
                if temperatures[j] > temp:
                    answer[i] = cnt          
                    break
                cnt += 1
                
        return answer