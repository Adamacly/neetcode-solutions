class PrefixTree:

    def __init__(self):
        self.elements = set()
        

    def insert(self, word: str) -> None:
        self.elements.add(word)


    def search(self, word: str) -> bool:
        if word in self.elements:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for s in self.elements:
            if s.startswith(prefix):
                return True
        return False
        
        