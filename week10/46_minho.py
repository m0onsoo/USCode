class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        answer = []

        def dfs(res: List[int], visited, answer) -> None:
            if len(visited) == len(nums):
                # print(res)
                answer.append(res.copy())
                return

            # print(res, visited)
            for num in nums:
                if num in visited:
                    continue

                visited.add(num)
                res.append(num)
                dfs(res, visited, answer)
                res.pop()
                visited.remove(num)

        dfs(res, visited, answer)
        return answer
            

        

        

        