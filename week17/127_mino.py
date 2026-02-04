class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        queue = deque()
        word_dict = defaultdict(list)
        visited = set()

        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                word_dict[pattern].append(word)

        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            curr, cnt = queue.popleft()

            if curr == endWord:
                return cnt

            for i in range(n):
                pattern = curr[:i] + "*" + curr[i+1:]

                for neighbor in word_dict[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, cnt + 1))

                word_dict[pattern] = []

        return 0