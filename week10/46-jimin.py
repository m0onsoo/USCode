# https://leetcode.com/problems/permutations/


class Solution:
    # recursive 하게 해서 몇번째 인덱스부터 선택시 ~~ 이런식으로 할 수 있지 않을까
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(path, remaining):
            if len(remaining) == 0:
                ans.append(path)
            for num in remaining:
                next_list = remaining[:]
                next_list.remove(num)
                dfs(path + [num], next_list)

        dfs([], nums)

        return ans

    # GPT 답안 : used list
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ans = []

        def dfs(path):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i] == True:
                    continue
                used[i] = True
                dfs(path + [nums[i]])
                used[i] = False

        dfs([])

        return ans
