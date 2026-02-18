class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_letter_map = dict()
        curr_letter = "abcdefghijklmnopqrstuvwxyz"
        idx = 0
        for num in range(2, 10):
            cnt = 4 if num == 7 or num == 9 else 3
            key = str(num)
            for _ in range(cnt):
                if key not in digit_letter_map:
                    digit_letter_map[key] = []
                digit_letter_map[key].append(curr_letter[idx])
                idx += 1

        # print(digit_letter_map)
        n = len(digits)
        res = []
        def dfs(curr, ans):
            if curr == n:
                return res.append(ans)

            for letter in digit_letter_map[digits[curr]]:
                dfs(curr+1, ans+letter)

        dfs(0, "")
        # print(res)
        return res
        