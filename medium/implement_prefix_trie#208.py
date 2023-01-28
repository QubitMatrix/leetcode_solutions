class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        t=self.trie
        for x in word:
            if(x not in t):
                t[x]={}
            t=t[x]
        t['$']={}

    def search(self, word: str) -> bool:
        t=self.trie
        for x in word:
            if(x in t):
                t=t[x]
            else:
                return False
        return '$' in t

    def startsWith(self, prefix: str) -> bool:
        t=self.trie
        for x in prefix:
            if(x in t):
                t=t[x]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
