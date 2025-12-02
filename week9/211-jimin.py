# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# 211-design-add-and-search-words-data-structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def dfs(self, node, word):
        if len(word) == 0:
            return node.is_end
        else:
            if word[0] == ".":
                track = False
                for char in node.children:
                    track = track or self.dfs(node.children[char], word[1:])
                return track
            elif word[0] in node.children:
                return self.dfs(node.children[word[0]], word[1:])
            else:
                return False

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
