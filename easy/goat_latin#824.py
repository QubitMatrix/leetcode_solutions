class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new=""
        vow=['a','A','e','E','i','I','o','O','u','U']
        s=sentence.split()
        for x in range(len(s)):
            if(s[x][0] in vow):
                new+=s[x]+"ma"+"a"*(x+1)+" "
            else:
                new+=s[x][1:]+s[x][0]+"ma"+"a"*(x+1)+" "
        return new[:-1]
