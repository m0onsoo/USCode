from collections import deque, Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Constraints:
        # s: source string, p: pattern string
        # 1 <= len(s, p) <= 30,000 . no empty string as input
        # lower case only

        # Anagram:
        # exact same character and frequencies

        # s = "abcbad", p = "ab"
        # window = [], p_counter = {'a': 1, 'b': 1}, window_counter = {}
        # window = ['a'], window_counter = {'a': 1}
        # window = ['a', 'b'], window_counter = {'a': 1, 'b': 1}, answer = [0]
        # char = c / window = ['a', 'b', 'c'], window_counter = {'a': 1, 'b': 1, 'c': 1}
        # -> window = ['b', 'c'], window_counter = {'b': 1, 'c': 1}

        
        answer = []

        window = deque()
        p_counter = Counter(p)
        window_counter = defaultdict(int)

        for i, char in enumerate(s):
            window.append((i, char))
            window_counter[char] += 1

            while len(window) > len(p):
                _, pop_char = window.popleft()
                window_counter[pop_char] -= 1
                if window_counter[pop_char] == 0:
                    del window_counter[pop_char]

            if len(window) == len(p) and window_counter == p_counter:
                answer.append(window[0][0])   # start index of the window
        
        return answer