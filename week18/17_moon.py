from collections import deque

# 0ms, 19.34MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                }
        

        queue = deque(hashmap[digits[0]])
        for i in range(1, len(digits)):
            for _ in range(len(queue)):
                curr = queue.popleft()
                for char in hashmap[digits[i]]:
                    queue.append(curr + char)
        return list(queue)