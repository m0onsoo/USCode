# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Graph로 생각하면 어떨까?
        # 그래프로 만들고 최단거리 찾으면 될거같다. BFS로 찾으면 될거같은데?

        # def is_similar(a, b):
        #     if len(a) != len(b):
        #         return False

        #     count_a = Counter(a)
        #     count_b = Counter(b)
        #     diff_count = 0
        #     for char in count_a:
        #         print(a, b, char, count_a[char], count_b[char])
        #         if count_a[char] == count_b[char]:
        #             continue
        #         elif diff_count != 0:
        #             return False
        #         elif abs(count_a[char] - count_b[char]) > 1:
        #             return False
        #         else:
        #             diff_count += 1
        #     return True

        def is_similar(a, b):
            if len(a) != len(b):
                return False
            diff_count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff_count += 1
                if diff_count > 1:
                    return False
            return True

        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        n = len(wordList)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                # print(wordList[i], wordList[j], is_similar(wordList[i], wordList[j]))
                if is_similar(wordList[i], wordList[j]):
                    # print(wordList[i], wordList[j])
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        seen = set()
        seen.add(beginWord)

        q = deque([beginWord])
        num_words = 1
        # print(graph)
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return num_words
                for nxt in graph[cur]:
                    if nxt in seen:
                        continue
                    q.append(nxt)
                    seen.add(nxt)
            num_words += 1

        return 0