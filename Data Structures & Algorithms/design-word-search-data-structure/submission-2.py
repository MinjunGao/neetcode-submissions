class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                idx = ord(c) - ord('a')
                if idx < 0 or idx >= 26 or not curr.children[idx]:
                    return False
                curr = curr.children[idx]
            return curr.is_word
        return dfs(0, self.root)