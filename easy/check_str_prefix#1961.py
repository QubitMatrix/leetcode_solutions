class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for x in range(1,len(s)+1):
            a="".join(words[0:x])
            if(a==s):
                return True
        return False
