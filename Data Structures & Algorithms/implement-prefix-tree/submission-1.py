class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        #self.elements = set()
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        #self.elements.add(word)

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # if word in self.elements:
        #     return True
        # return False

        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        # for s in self.elements:
        #     if s.startswith(prefix):
        #         return True
        # return False

        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        