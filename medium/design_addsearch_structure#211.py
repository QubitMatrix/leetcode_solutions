class WordDictionary:

    def __init__(self):
        self.trie={}

    def addWord(self, word: str) -> None:
        t=self.trie
        for x in word:
            if(x not in t):
                t[x]={}
            t=t[x]
        t['$']={}

    def search(self, word: str) -> bool:
        bool1=False
        t=self.trie
        def search_suffix(new_word,new_trie):
            bool2=False
            tt=new_trie
            if(new_word==""):
                return '$' in tt
            for xx in range(len(new_word)):
                if(new_word[xx]=='.'):
                    for yy in tt:
                        if(yy=='$'):
                            continue
                        bool2=search_suffix(new_word[xx+1:],tt[yy])
                        if(bool2):
                            break
                    return bool2
                else:
                    if(new_word[xx] not in tt):
                        return False
                    else:
                        tt=tt[new_word[xx]]
            return '$' in tt    
            
        for x in range(len(word)):
            if(word[x]!='.' and word[x] not in t):
                return False
            if(word[x]!='.' and word[x] in t):
                t=t[word[x]]
            else:
                for y in t:
                    bool1=search_suffix(word[x+1:],t[y])
                    if(bool1):
                        break
                return bool1
        return '$' in t



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
