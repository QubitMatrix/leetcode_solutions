class Solution:
    def insert(self,trie,word):
        for x in word:
            if(x not in trie):
                trie[x]={}
            trie=trie[x]
        trie['$']={}#eow
    def search(self,word,start,stop,trie,org_trie):
        if(start>=stop):
            return '$' in trie
        if(word[start] in trie):
            if(self.search(word,start+1,stop,trie[word[start]],org_trie)):
                return True
        if('$' in trie):
            return self.search(word,start,stop,org_trie,org_trie)
        return False    
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans=[]
        trie={}
        words.sort(key=lambda x:len(x))
        for word in words:
            if(self.search(word,0,len(word),trie,trie)):
                ans.append(word)
            self.insert(trie,word)

        return ans
