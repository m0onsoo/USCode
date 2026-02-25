# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
            }


        ans = []
        def dfs(start, path):
            if start == len(digits):
                ans.append(path[:])
                return
            digit = digits[start]
            chars = comb[digit]
            for char in chars:
                dfs(start + 1, path + char)

        dfs(0, '')

        return ans