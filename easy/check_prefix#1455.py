class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split()
        for x in range(len(words)):
            if(words[x][0:len(searchWord)]==searchWord):
                return x+1
        return -1
