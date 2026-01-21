from collections import deque, defaultdict, Counter
import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        target = len(set(t))

        satisfied = 0
        window = deque()
        sub_counter = defaultdict(int)

        result = ""
        length = sys.maxsize
        for i, char in enumerate(s):
            window.append(char)
            if char in counter.keys():
                # char가 t에 포함되는 문자일 때, 서브스트링 카운터 +1
                sub_counter[char] += 1

                if sub_counter[char] == counter[char]:
                    # 서브스트링 카운터가 원본 카운터와 일치하면, 조건을 충족하는 변수 +1
                    satisfied += 1

                    while satisfied == target:
                        # 조건 충족한 문자의 수가 타겟과 같으면
                        pop = window.popleft()
                        if pop in counter.keys():
                            sub_counter[pop] -= 1
                            if sub_counter[pop] < counter[pop]:
                                substring = pop + "".join(window)
                                if len(substring) < length:
                                    result = substring
                                    length = len(substring)
                                satisfied -= 1

        return result
    