class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=""
        l1=0
        while(l1<len(word1) and l1<len(word2)):
            word3+=word1[l1]+word2[l1]
            l1+=1
        if(l1<len(word1)):
            word3+=word1[l1:]
        if(l1<len(word2)):
            word3+=word2[l1:]
        return word3
